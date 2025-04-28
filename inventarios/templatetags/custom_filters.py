from django import template

register = template.Library()

@register.filter
def sum_movimientos(movimientos):
    total = 0
    for movimiento in movimientos:
        if movimiento.tipo == 'ENTRADA' or movimiento.tipo == 'AJUSTE' or movimiento.tipo == 'TRASPASO':
            total += movimiento.cantidad or 0
        elif movimiento.tipo == 'SALIDA':
            total -= movimiento.cantidad or 0
    return total
