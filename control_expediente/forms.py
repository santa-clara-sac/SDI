from django import forms
from .models import CasoJudicial, Seguimiento, Gasto, Presentacion, GastoPresentacion
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
        exclude = ['caso', 'fecha_registro']
        widgets = {
            'fecha_seguimiento': forms.DateInput(attrs={'type': 'date'}),
            'inter': forms.CheckboxInput(attrs={
                'class': 'form-check-input switch-color',
                'role': 'switch',
                'id': 'id_inter'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'inter':  # evitar poner form-control al switch
                field.widget.attrs['class'] = 'form-control'

        self.fields['responsable'].required = False
        self.fields['seguimiento'].required = False
        self.fields['pdf'].required = False



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
        # Marcar explícitamente como no requerido
        self.fields['sustento'].required = False
        self.fields['gastos_dolares'].required = False

########################################################################################################

class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        exclude = ['caso']  # Excluye campos automáticos
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Agregar clases CSS
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class GastoPresentacionForm(forms.ModelForm):
    class Meta:
        model = GastoPresentacion
        exclude = ['presentacion', 'fecha_registro', 'seguimiento']  # seguimiento lo asignaremos en la vista
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
