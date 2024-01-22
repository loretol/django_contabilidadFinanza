from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")



def factura(request):
    return render(request, "factura.html")


def factorVenta(request):
    return render(request, "factorVenta.html")