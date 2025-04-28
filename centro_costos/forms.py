from django import forms
from .models import Actividad, Gasto, CantaCallao, NuevoGasto, GastoN1, GastoN2, GastoN3

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
        
class NuevoGastoForm(forms.ModelForm):
    class Meta:
        model = NuevoGasto
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'style': 'margin-bottom: 10px;'
            }),
        }


##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

class GastoN1Form(forms.ModelForm):
    class Meta:
        model = GastoN1
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN2Form(forms.ModelForm):
    class Meta:
        model = GastoN2
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN3Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN4Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN5Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN6Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN7Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN8Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN9Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GastoN10Form(forms.ModelForm):
    class Meta:
        model = GastoN3
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'