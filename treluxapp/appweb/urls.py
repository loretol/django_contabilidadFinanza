from django.urls import path
from.views import home,factura,factorVenta

urlpatterns =[

    path('home/', home, name="home"),
    path('', home, name="home"),
    path('factura/', factura, name="factura"),
    path('factorVenta/', factorVenta, name="factorVenta"),
]