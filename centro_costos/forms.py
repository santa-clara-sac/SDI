from django import forms
from .models import Actividad, Gasto

# class ResponsableForm(forms.ModelForm):
#     class Meta:
#         model = Responsable
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

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
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Estilizar todos los campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'