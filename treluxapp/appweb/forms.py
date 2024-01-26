from django import forms
from .models import *
from django.utils import timezone


class FacturaForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d', 'disabled': 'true'}),
        label='Fecha de Vencimiento'
    )

    class Meta:
        model = Factura
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Establecer la fecha de emisión como el día actual
        self.fields['fecha_emision'].widget = forms.DateInput(attrs={'type': 'date', 'value': timezone.now().strftime('%Y-%m-%d'), 'disabled': 'true'})

        # Calcular la fecha de vencimiento como la fecha actual más 30 días
        fecha_vencimiento = timezone.now() + timezone.timedelta(days=30)
        self.fields['fecha_vencimiento'].widget = forms.DateInput(attrs={'type': 'date', 'value': fecha_vencimiento.strftime('%Y-%m-%d'), 'disabled': 'true'})




class FactorProductoForm(forms.ModelForm):

    class Meta:
        model = FactorProducto
        fields = "__all__"

        widgets = {
            'id_producto': forms.HiddenInput(),
            'fecha_modificacion': forms.DateInput(attrs={'type': 'date', 'disabled': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Establecer la fecha de modificación como el día actual
        self.initial['fecha_modificacion'] = timezone.now().strftime('%Y-%m-%d')