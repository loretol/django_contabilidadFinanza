from django.db import models

# Create your models here.


class Salud(models.Model):
    id_salud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - Porcentaje: {self.porcentaje}"

class AFP(models.Model):
    id_afp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - Porcentaje: {self.porcentaje}"
class Empleado(models.Model):
    rut_empleado = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    Fecha_Nacimiento = models.DateField(null=True, blank=True)
    Area_Desempeno = models.CharField(max_length=50, null=True, blank=True)
    Sueldo_Base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Direccion = models.CharField(max_length=255, null=True, blank=True)
    Fecha_Ingreso = models.DateField(null=True, blank=True)
    Dias_Vacaciones = models.IntegerField(null=True, blank=True)
    id_salud = models.ForeignKey(Salud, on_delete=models.SET_NULL, null=True, blank=True)
    id_afp = models.ForeignKey(AFP, on_delete=models.SET_NULL, null=True, blank=True)
    Bonificacion = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Comisiones = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Fecha_Contrato = models.DateField(null=True, blank=True)
    Correo = models.EmailField(unique=True)
    Clave_Usuario = models.CharField(max_length=50)
    Especializacion = models.CharField(max_length=50, null=True, blank=True)
    Area_A_Cargo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - Rut: {self.rut_empleado}"
    

class Produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)
    Rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Producción #{self.id_produccion} - Producto: {self.nombre_producto},Cantidad: {self.cantidad}, Total: {self.total}"
    

class PuntoVenta(models.Model):
    id_p_venta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    encargado = models.CharField(max_length=150)

    def __str__(self):
        return f"Punto de Venta #{self.id_p_venta} - Nombre: {self.nombre}, Encargado: {self.encargado}"    
    
class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f"Bodega #{self.id_bodega} - Nombre: {self.nombre_bodega}, Dirección: {self.direccion}"
    

class OrdenRequisicion(models.Model):
    id_requisicion = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    fecha_despacho = models.DateField(null=True, blank=True)
    productos = models.TextField()
    entregado_por = models.CharField(max_length=150)
    recibido_por = models.CharField(max_length=150)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"Orden de Requisición #{self.id_requisicion} - Pedido: {self.fecha_pedido}, Despacho: {self.fecha_despacho}, Bodega: {self.id_bodega}"
    

class OrdenProduccion(models.Model):
    id_orden_produc = models.AutoField(primary_key=True)
    fecha = models.DateField()
    productos_usados = models.TextField()
    personal_de_trabajo = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"Orden de Producción #{self.id_orden_produc} - Fecha: {self.fecha}, Bodega: {self.id_bodega}, Estado: {self.estado}"
    

class LiquidacionSueldo(models.Model):
    id_liquidacion = models.AutoField(primary_key=True)
    rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Sueldo_Base = models.DecimalField(max_digits=10, decimal_places=2)
    Comisiones = models.DecimalField(max_digits=10, decimal_places=2)
    id_afp = models.ForeignKey(AFP, on_delete=models.CASCADE)
    id_salud = models.ForeignKey(Salud, on_delete=models.CASCADE)
    dias_trabajados = models.IntegerField()
    Base_Imponible = models.DecimalField(max_digits=10, decimal_places=2)
    Descuentos = models.DecimalField(max_digits=10, decimal_places=2)
    Total_Haberes = models.DecimalField(max_digits=10, decimal_places=2)
    Liquido_A_Pago = models.DecimalField(max_digits=10, decimal_places=2)
    Bonificaciones = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_periodo = models.DateField()

    def __str__(self):
        return f"Liquidación #{self.id_liquidacion} - Rut: {self.rut_empleado}, Período: {self.fecha_periodo}"



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100, null=False, blank=False)
    descripcion_producto = models.CharField(max_length=300, null=False, blank=False)
    stock = models.IntegerField()
    posicion = models.CharField(max_length=10, null=False, blank=False)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def __str__(self):
        return f"Producto #{self.id_producto} - Nombre: {self.nombre_producto}, Stock: {self.stock}, Bodega: {self.id_bodega}"
    

class OrdenCompra(models.Model):
    id_orden_Comp = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden de Compra #{self.id_orden_Comp} - Cantidad: {self.cantidad}, Producto: {self.id_producto}"
    


class FactorProducto(models.Model):
    id_factor_prod = models.AutoField(primary_key=True)
    factor_venta = models.FloatField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=20, null=False, blank=False)
    precio_unitario = models.IntegerField()
    fecha_modificacion = models.DateField()

    def __str__(self):
        return f"Factor Producto #{self.id_factor_prod} - Producto: {self.nombre_producto}, Factor Venta: {self.factor_venta}, Precio Unitario: {self.precio_unitario}"
    

class Cliente(models.Model):
    run_cliente = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} - RUN: {self.run_cliente}"
    


class NotaVenta(models.Model):
    id_n_venta = models.AutoField(primary_key=True)
    run_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    rut_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    importe = models.IntegerField()
    sub_total = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return f"Nota de Venta #{self.id_n_venta} - Cliente: {self.run_cliente.nombre} {self.run_cliente.apellido}, Empleado: {self.rut_empleado.nombre} {self.rut_empleado.apellidos}, Fecha: {self.fecha}"
    

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=20)
    id_cliente = models.IntegerField()
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    descripcion_producto = models.CharField(max_length=100)
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=20)
    cantidad_producto = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=20)
    metodo_pago = models.CharField(max_length=20)
    IVA = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    id_n_venta = models.ForeignKey(NotaVenta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura #{self.id_factura} - Cliente: {self.nombre_cliente}, Fecha de Emisión: {self.fecha_emision}, Monto Total: {self.monto_total}"