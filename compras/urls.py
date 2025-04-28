from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_compras, name='compras'),
    # PROVEEDORES
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    # ORDENES DE COMPRA
    path('ordenes_compra/', views.lista_ordenes_compra, name='lista_ordenes_compra'),
    path('orden_compra/crear/', views.crear_orden_compra, name='crear_orden_compra'),
    path('orden_compra/<int:orden_id>/', views.ver_orden_compra, name='ver_orden_compra'),
    path('orden_compra/<int:orden_id>/recepcion/', views.recepcion_productos, name='recepcion_productos'),
    path('ordenes_compra/pendientes/', views.ordenes_pendientes, name='ordenes_pendientes'),
]
