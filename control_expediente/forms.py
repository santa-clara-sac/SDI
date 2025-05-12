from django import forms
from .models import CasoJudicial, Seguimiento, Gasto
from django.utils.timezone import now


class CasoJudicialForm(forms.ModelForm):
    class Meta:
        model = CasoJudicial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        exclude = ['caso', 'fecha_registro']  # Excluye campos automáticos
        widgets = {
            'fecha_seguimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Opcional: establecer fecha_seguimiento por defecto
        if not self.fields['fecha_seguimiento'].initial:
            self.fields['fecha_seguimiento'].initial = now().date()
        
        # Agregar clases CSS
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        exclude = ['fecha_registro', 'seguimiento']  # seguimiento lo asignaremos en la vista
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'