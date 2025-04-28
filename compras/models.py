from django.db import models

class Proveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    condiciones_pago = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre or "Proveedor sin nombre"


class OrdenCompra(models.Model):
    ESTADOS = [
        ('ABIERTA', 'Abierta'),
        ('PARCIAL', 'Parcialmente Recibida'),
        ('CERRADA', 'Cerrada'),
        ('CANCELADA', 'Cancelada'),
    ]

    id = models.BigAutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_emision = models.DateField(null=True, blank=True)
    fecha_entrega_estimada = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ABIERTA')
    observaciones = models.TextField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OC-{self.id} ({self.proveedor.nombre if self.proveedor else 'Sin proveedor'})"


class OrdenCompraDetalle(models.Model):
    id = models.BigAutoField(primary_key=True)
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('inventarios.Producto', on_delete=models.SET_NULL, null=True, blank=True)
    cantidad_pedida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cantidad_recibida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Detalle OC-{self.orden_compra.id} | {self.producto.sku if self.producto else 'Sin producto'}"
