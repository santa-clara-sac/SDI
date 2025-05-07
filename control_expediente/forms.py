from django import forms
from .models import CasoJudicial

class CasoJudicialForm(forms.ModelForm):
    class Meta:
        model = CasoJudicial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'