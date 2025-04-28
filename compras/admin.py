from django.contrib import admin
from .models import Proveedor, OrdenCompra, OrdenCompraDetalle

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rfc', 'contacto', 'telefono', 'email', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'rfc', 'contacto', 'email')

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'fecha_emision', 'fecha_entrega_estimada', 'estado', 'creado_en')
    list_filter = ('estado', 'proveedor')
    search_fields = ('id', 'proveedor__nombre')
    date_hierarchy = 'fecha_emision'

@admin.register(OrdenCompraDetalle)
class OrdenCompraDetalleAdmin(admin.ModelAdmin):
    list_display = ('orden_compra', 'producto', 'cantidad_pedida', 'cantidad_recibida', 'precio_unitario')
    list_filter = ('orden_compra', 'producto')
    search_fields = ('orden_compra__id', 'producto__sku')
