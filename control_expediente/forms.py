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
        self.fields['sede'].required = False


class SeguimientoForm(forms.ModelForm):
    resolucion_tipo = forms.ChoiceField(
        choices=[('Escrito', 'Escrito'), ('Resolución', 'Resolución')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    resolucion_texto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    )

    class Meta:
        model = Seguimiento
        exclude = ['caso', 'fecha_registro']
        widgets = {
            'fecha_seguimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_pendiente': forms.DateInput(attrs={'type': 'date'}),
            'inter': forms.CheckboxInput(attrs={
                'class': 'form-check-input switch-color',
                'role': 'switch',
                'id': 'id_inter'
            }),
            'resolucion': forms.HiddenInput(),  # 👈 Ocultamos el campo real
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name not in ['inter', 'resolucion_tipo', 'resolucion_texto']:
                field.widget.attrs['class'] = 'form-control'

        self.fields['responsable'].required = False
        self.fields['seguimiento'].required = False
        self.fields['fecha_seguimiento'].required = False
        self.fields['pdf'].required = False

    def clean(self):
        cleaned_data = super().clean()
        tipo = self.cleaned_data.get('resolucion_tipo')
        texto = self.cleaned_data.get('resolucion_texto')

        if tipo and texto:
            cleaned_data['resolucion'] = f"{tipo} {texto.strip()}"
            
            # 👇 Asigna automáticamente el valor de inter según el tipo
            cleaned_data['inter'] = True if tipo.lower() == 'resolución' else False

        elif tipo or texto:
            self.add_error('resolucion_texto', 'Completa ambos campos de resolución')

        return cleaned_data






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
