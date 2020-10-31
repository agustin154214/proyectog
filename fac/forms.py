from django import forms

from .models import Cliente,Menu

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombre_centro','numero_centro','nivel',
            'contacto','estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields=['nombre_menu', 'estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })