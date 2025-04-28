from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, Movimiento, Almacen, CategoriaProducto
from django.db.models import Sum
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


def index(request):
    return render(request, 'inventarios/index.html')

#buscador
def buscar_global(request):
    query = request.GET.get('q', '')

    if not query:
        return redirect('inventario_index')
    # Buscar en productos
    resultados_productos = Producto.objects.filter(
            Q(descripcion__icontains=query) |
            Q(sku__icontains=query) |
            Q(clasificacion__icontains=query) |
            Q(tipo__icontains=query)
    )

    # Buscar en movimientos
    resultados_movimientos = Movimiento.objects.filter(
            Q(referencia__icontains=query) |
            Q(observaciones__icontains=query) |
            Q(producto__descripcion__icontains=query)
    )

    # Buscar en almacenes
    resultados_almacenes = Almacen.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
    )


    context = {
        'query': query,
        'resultados_productos': resultados_productos,
        'resultados_movimientos': resultados_movimientos,
        'resultados_almacenes': resultados_almacenes,
    }
    return render(request, 'inventarios/buscar_resultados.html', context)


# sección de inventarios
def almacenes(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        try:
            if not codigo or not nombre:
                raise ValueError("Código y nombre son obligatorios.")

            Almacen.objects.create(
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
                activo=True
            )
            messages.success(request, "Almacén registrado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al registrar el almacén: {str(e)}")

        return redirect('almacenes')

    almacenes = Almacen.objects.all()
    return render(request, 'inventarios/almacenes.html', {'almacenes': almacenes})


def productos(request):
    if request.method == 'POST':
        if 'sku' in request.POST:
            # Registro de producto
            sku = request.POST.get('sku')
            descripcion = request.POST.get('descripcion')
            unidad_medida = request.POST.get('unidad_medida')
            tipo = request.POST.get('tipo')
            categoria_id = request.POST.get('categoria')

            try:
                if not sku or not tipo:
                    raise ValueError("SKU y Tipo son obligatorios.")

                categoria = CategoriaProducto.objects.get(id=categoria_id) if categoria_id else None

                Producto.objects.create(
                    sku=sku,
                    descripcion=descripcion,
                    unidad_medida=unidad_medida,
                    tipo=tipo,
                    categoria=categoria,
                    activo=True
                )
                messages.success(request, "Producto registrado correctamente.")
            except Exception as e:
                messages.error(request, f"Error al registrar el producto: {str(e)}")

        elif 'nombre_categoria' in request.POST:
            # Registro de categoría
            nombre_categoria = request.POST.get('nombre_categoria')
            try:
                if not nombre_categoria:
                    raise ValueError("El nombre de la categoría no puede estar vacío.")
                CategoriaProducto.objects.create(nombre=nombre_categoria)
                messages.success(request, "Categoría agregada exitosamente.")
            except Exception as e:
                messages.error(request, f"Error al agregar categoría: {str(e)}")

        return redirect('productos')

    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()
    return render(request, 'inventarios/productos.html', {
        'productos': productos,
        'categorias': categorias
    })


def control_inventario(request):
    productos = Producto.objects.all()
    almacenes = Almacen.objects.all()
    ultimos_movimientos = Movimiento.objects.select_related('producto', 'almacen').order_by('-fecha')[:10]

    if request.method == 'POST':
        if 'crear_almacen' in request.POST:
            codigo = request.POST.get('nuevo_codigo')
            nombre = request.POST.get('nuevo_nombre')
            descripcion = request.POST.get('nuevo_descripcion')

            try:
                Almacen.objects.create(
                    codigo=codigo,
                    nombre=nombre,
                    descripcion=descripcion,
                    activo=True
                )
                messages.success(request, "Nuevo almacén creado exitosamente.")
            except Exception as e:
                messages.error(request, f"Error al crear almacén: {e}")
            return redirect('control_inventario')

        else:
            try:
                tipo = request.POST.get('tipo')
                producto_id = request.POST.get('producto')
                cantidad = float(request.POST.get('cantidad'))
                almacen_id = request.POST.get('almacen')
                referencia = request.POST.get('referencia')

                producto = Producto.objects.get(id=producto_id)
                almacen = Almacen.objects.get(id=almacen_id)

                # Validación para salida: que no saque más de lo que hay
                if tipo == 'SALIDA' and producto.stock_actual < cantidad:
                    messages.error(request, f"No hay suficiente stock para realizar la salida. Stock actual: {producto.stock_actual}")
                    return redirect('control_inventario')

                # Crear el movimiento
                Movimiento.objects.create(
                    tipo=tipo,
                    producto=producto,
                    almacen=almacen,
                    cantidad=cantidad,
                    referencia=referencia
                )

                # Actualizar stock del producto
                if tipo == 'ENTRADA':
                    producto.stock_actual += cantidad
                elif tipo == 'SALIDA':
                    producto.stock_actual -= cantidad
                elif tipo == 'AJUSTE':
                    producto.stock_actual = cantidad  # Puedes cambiar esta lógica si se requiere otra política
                # Traspaso no afecta el stock total aquí porque no se está gestionando origen/destino

                producto.save()

                messages.success(request, "Movimiento registrado correctamente.")
            except Exception as e:
                messages.error(request, f"Error al registrar el movimiento: {e}")
            return redirect('control_inventario')

    return render(request, 'inventarios/control.html', {
        'productos': productos,
        'almacenes': almacenes,
        'ultimos_movimientos': ultimos_movimientos
    })


def cargar_productos_excel(request):
    if request.method == 'POST' and request.FILES.get('archivo_excel'):
        archivo = request.FILES['archivo_excel']
        fs = FileSystemStorage()
        filename = fs.save(archivo.name, archivo)
        ruta_archivo = fs.path(filename)

        try:
            df = pd.read_excel(ruta_archivo)
            creados = 0
            for _, row in df.iterrows():
                sku = str(row["CODIGO"]).strip()
                descripcion = str(row["DESCRIPCIÓN"]).strip()
                unidad_medida = str(row["INVENTARIO"]).strip()

                if sku and descripcion:
                    _, creado = Producto.objects.get_or_create(
                        sku=sku,
                        defaults={
                            "descripcion": descripcion,
                            "unidad_medida": unidad_medida,
                            "tipo": "MP",
                            "activo": True
                        }
                    )
                    if creado:
                        creados += 1
            messages.success(request, f"Productos creados correctamente: {creados}")
        except Exception as e:
            messages.error(request, f"Error al procesar archivo: {str(e)}")
        return redirect('cargar_productos_excel')

    return render(request, 'inventarios/cargar_productos_excel.html')


def lista_movimientos(request):
    movimientos = Movimiento.objects.all().order_by('-fecha')
    return render(request, 'inventarios/movimientos.html', {'movimientos': movimientos})


def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    almacenes = Almacen.objects.all()
    movimientos = Movimiento.objects.filter(producto=producto).order_by('-fecha')

    # Stock por almacén
    stock_por_almacen = (
        Movimiento.objects
        .filter(producto=producto)
        .values('almacen__codigo', 'almacen__nombre')
        .annotate(total=Sum('cantidad')) 
        .order_by('almacen__codigo')
    )

    return render(request, 'inventarios/producto_detalle.html', {
        'producto': producto,
        'movimientos': movimientos,
        'stock_por_almacen': stock_por_almacen,
    })
