from django import forms
from .models import Actividad, Gasto, CantaCallao, GastoGeneral, GastoTA, GastoCC, GastoBR

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Estilizar todos los campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # Obligatorio: no permitir dejar vacío
        self.fields['tipo'].required = True
        self.fields['responsable'].required = False

        # Eliminar la opción vacía por defecto y poner la personalizada
        choices = self.fields['tipo'].choices
        filtered_choices = [choice for choice in choices if choice[0] != '']
        self.fields['tipo'].choices = [('', 'Seleccione tipo de gasto')] + filtered_choices

        # Personalizar etiqueta vacía para el campo ForeignKey
        #self.fields['responsable'].empty_label = "Seleccione responsable"

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['actividad', 'item', 'fecha', 'detalle', 'documento', 'debe', 'haber', 'tipo_gasto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['actividad'].empty_label = "Seleccione actividad"

        # Estilizar todos los campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CantaCallaoForm(forms.ModelForm):
    class Meta:
        model = CantaCallao
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
class GastoGeneralForm(forms.ModelForm):
    class Meta:
        model = GastoGeneral
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


###############################################################################################
class GastoTAForm(forms.ModelForm):
    class Meta:
        model = GastoTA
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoCCForm(forms.ModelForm):
    class Meta:
        model = GastoCC
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class GastoBRForm(forms.ModelForm):
    class Meta:
        model = GastoBR
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


