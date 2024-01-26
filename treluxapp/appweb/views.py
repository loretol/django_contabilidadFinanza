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

