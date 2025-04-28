from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventario_index'),
    
    #buscardor
    path('buscar/', views.buscar_global, name='buscar_global'),

    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),

    # sección de almacenes
    path('almacenes/', views.almacenes, name='almacenes'),

    path('productos/', views.productos, name='productos'),

    path('cargar_productos_excel/', views.cargar_productos_excel, name='cargar_productos_excel'),

    path('movimientos/', views.lista_movimientos, name='lista_movimientos'),

    path('control_inventario/', views.control_inventario, name='control_inventario'),

    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),
]
