from django.db import models

# Almacén: ejemplo "00 - Producto terminado"
class Almacen(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# 
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# Producto básico con SKU y descripción
class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku = models.CharField(max_length=30, unique=True, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    unidad_medida = models.CharField(max_length=20, null=True, blank=True)
    stock_minimo = models.PositiveIntegerField(default=0, null=True, blank=True)
    clasificacion = models.CharField(max_length=5, null=True, blank=True, help_text="Ej. A, B, C, etc.")
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey('CategoriaProducto', on_delete=models.SET_NULL, null=True, blank=True)

    TIPO_CHOICES = [
        ('PT', 'Producto Terminado'),
        ('MP', 'Materia Prima'),
        ('SV', 'Servicio'),
    ]
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, null=True, blank=True)
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.sku} - {self.descripcion or 'Sin descripción'}"



# Ubicación dentro de almacén (rack, pasillo, bin, etc.)
class Ubicacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    almacen = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, blank=True)
    codigo = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.almacen} / {self.codigo}"


# Movimiento de inventario: entrada o salida
class Movimiento(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
        ('TRASPASO', 'Traspaso'),
    ]

    id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    almacen = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    referencia = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.producto} ({self.cantidad})"
