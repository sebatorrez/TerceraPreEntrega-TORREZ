from django import forms
from .models import Usuario, Filial

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = ['nombre_filial', 'direccion']

    def __init__(self, *args, **kwargs):
        super(FilialForm, self).__init__(*args, **kwargs)
        self.fields['nombre_filial'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
    
    


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'filial_asociada']

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['apellido'].widget.attrs['class'] = 'form-control'
        self.fields['filial_asociada'].widget.attrs['class'] = 'form-control'
