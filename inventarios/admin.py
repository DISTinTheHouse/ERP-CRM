from django.contrib import admin
from .models import Almacen, Producto, Ubicacion, Movimiento, CategoriaProducto

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nombre', 'descripcion', 'activo']
    search_fields = ['codigo', 'nombre']
    list_filter = ['activo']
    ordering = ['codigo']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'descripcion', 'tipo', 'unidad_medida', 'stock_minimo', 'clasificacion', 'categoria', 'activo')
    list_filter = ('tipo', 'activo', 'clasificacion', 'categoria')
    search_fields = ('sku', 'descripcion')

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'almacen', 'codigo', 'descripcion']
    search_fields = ['codigo', 'descripcion']
    list_filter = ['almacen']
    ordering = ['almacen', 'codigo']

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'fecha', 'tipo', 'producto', 'cantidad', 
        'almacen', 'ubicacion', 'referencia'
    ]
    search_fields = ['producto__sku', 'producto__descripcion', 'referencia']
    list_filter = ['tipo', 'almacen', 'producto']
    ordering = ['-fecha']
    date_hierarchy = 'fecha'