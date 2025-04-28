from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, OrdenCompra, OrdenCompraDetalle
from inventarios.models import Producto
from django.contrib import messages
from django.http import JsonResponse


def index_compras(request):
    return render(request, 'compras/index_compras.html')


# PROVEEDORES
def lista_proveedores(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rfc = request.POST.get('rfc')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        condiciones_pago = request.POST.get('condiciones_pago')

        Proveedor.objects.create(
            nombre=nombre,
            rfc=rfc,
            contacto=contacto,
            telefono=telefono,
            email=email,
            direccion=direccion,
            condiciones_pago=condiciones_pago
        )

        messages.success(request, '✅ Proveedor agregado correctamente.')

        return redirect('lista_proveedores')

    proveedores = Proveedor.objects.all()
    return render(request, 'compras/lista_proveedores.html', {'proveedores': proveedores})

    return render(request, 'compras/lista_proveedores.html', {'proveedores': proveedores})



# ORDENES DE COMPRA
def lista_ordenes_compra(request):
    proveedores = Proveedor.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)
    ordenes = OrdenCompra.objects.select_related('proveedor').all()

    return render(request, 'compras/lista_ordenes_compra.html', {
        'ordenes': ordenes,
        'proveedores': proveedores,
        'productos': productos
    })

def crear_orden_compra(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        fecha_entrega = request.POST.get('fecha_entrega')
        observaciones = request.POST.get('observaciones')

        orden = OrdenCompra.objects.create(
            proveedor_id=proveedor_id,
            fecha_entrega_estimada=fecha_entrega,
            observaciones=observaciones
        )

        productos_ids = request.POST.getlist('producto_id')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')

        for idx, producto_id in enumerate(productos_ids):
            if producto_id:
                OrdenCompraDetalle.objects.create(
                    orden_compra=orden,
                    producto_id=producto_id,
                    cantidad_pedida=cantidades[idx],
                    precio_unitario=precios[idx]
                )

        return JsonResponse({'success': True, 'message': 'Orden de compra creada exitosamente.'})

    return JsonResponse({'success': False}, status=400)



def ver_orden_compra(request, orden_id):
    orden = get_object_or_404(OrdenCompra, id=orden_id)
    detalles = orden.detalles.all()
    return render(request, 'compras/ver_orden_compra.html', {'orden': orden, 'detalles': detalles})


def recepcion_productos(request, orden_id):
    orden = get_object_or_404(OrdenCompra, id=orden_id)
    detalles = orden.detalles.all()

    if request.method == 'POST':
        error = False  # Bandera para saber si hubo un error

        for detalle in detalles:
            cantidad_recibida = request.POST.get(f'cantidad_recibida_{detalle.id}')

            if cantidad_recibida:
                cantidad_recibida = float(cantidad_recibida)

                cantidad_total = (detalle.cantidad_recibida or 0) + cantidad_recibida

                if cantidad_total > detalle.cantidad_pedida:
                    error = True
                    messages.error(request, f"No puedes recibir más de lo pedido para el producto {detalle.producto.sku}.")
                else:
                    detalle.cantidad_recibida = cantidad_total
                    detalle.save()

        if error:
            # Si hubo error, regresamos a la misma pantalla
            return redirect('recepcion_productos', orden_id=orden.id)

        # Verificar si todos los productos están completamente recibidos
        detalles_actualizados = orden.detalles.all()
        if all(d.cantidad_recibida >= d.cantidad_pedida for d in detalles_actualizados):
            orden.estado = 'CERRADA'
        else:
            orden.estado = 'PARCIAL'
        
        orden.save()

        return redirect('ver_orden_compra', orden_id=orden.id)

    return render(request, 'compras/recepcion_productos.html', {'orden': orden, 'detalles': detalles})


def ordenes_pendientes(request):
    pendientes = OrdenCompra.objects.filter(estado__in=['ABIERTA', 'PARCIAL']).select_related('proveedor')

    return render(request, 'compras/ordenes_pendientes.html', {
        'pendientes': pendientes
    })
