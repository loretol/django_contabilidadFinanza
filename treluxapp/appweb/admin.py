from django.contrib import admin
from .models import * 

# Register your models here.

class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id_factura', 'nombre_cliente', 'fecha_emision', 'monto_total', 'estado_pago', 'metodo_pago']
    list_editable = ['estado_pago']
    list_filter = ['estado_pago', 'fecha_emision']
    search_fields = ['nombre_cliente', 'id_factura']



class FactorProductoAdmin(admin.ModelAdmin):
    list_display = ['id_factor_prod', 'nombre_producto', 'factor_venta', 'precio_unitario', 'precio_final', 'fecha_modificacion']
    list_filter = ['fecha_modificacion']
    search_fields = ['nombre_producto', 'id_factor_prod']



admin.site.register(Salud)
admin.site.register(AFP)
admin.site.register(Empleado)
admin.site.register(Produccion)
admin.site.register(PuntoVenta)
admin.site.register(Bodega)
admin.site.register(OrdenRequisicion)
admin.site.register(OrdenProduccion)
admin.site.register(LiquidacionSueldo)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(FactorProducto,FactorProductoAdmin)
admin.site.register(Cliente)
admin.site.register(NotaVenta)
admin.site.register(Factura,FacturaAdmin)








