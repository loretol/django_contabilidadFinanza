from django.shortcuts import render
from .models import Factura 
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")



def factura(request):
     
     #se crea una valiable llamada facts
    
    data = {
        'form':FacturaForm
    }
    if request.method == "POST":
        formulario = FacturaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "La factura se ha guardado"
        else:
            data["mensaje"] = "Ha ocurrido un error!!!"
            data["form"] = formulario
    
    return render(request, "factura.html", data)


def factorVenta(request):

    data = {
        'form':FactorProductoForm
    }
    return render(request, "factorVenta.html",data)



def gestionFactura(request):

    facts= Factura.objects.all()
    # se crea una consulta SQL

    facts= Factura.objects.raw("select * from appweb Factura")

     # creamos un objeto para enviar al template
    data = {
        'facts': facts
    }
    return render(request, "gestionfactura.html",data)

def crear_factura(request):
    if request.method == "POST":
        formulario = FacturaForm(data=request.POST)

        if formulario.is_valid():
            factura = formulario.save(commit=False)

            # Calcula el IVA utilizando la función de utilidad
            monto_total = factura.monto_total  # Ajusta según el nombre real del campo en tu modelo
            porcentaje_iva = 19.0  # Puedes ajustar el porcentaje de IVA según tus necesidades
            iva_calculado = (monto_total, porcentaje_iva)

            # Asigna el IVA calculado al campo correspondiente en tu modelo de factura
            factura.iva = iva_calculado

            # Guarda la factura con el IVA calculado
            factura.save()

            # Resto de la lógica para mostrar o redirigir como sea necesario
            return render(request, "factura_creada.html", {'factura': factura})

    else:
        formulario = FacturaForm()

    return render(request, "crear_factura.html", {'formulario': formulario})