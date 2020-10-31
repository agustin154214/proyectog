from django import forms

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = {'descripcion','estado'}
        labels = {'descripcion':"Descripcion de la categoría", "estado": "Estado"}
        widget={'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset= Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = {'categoria','descripcion','estado'}
        labels = {'descripcion':"Sub Categoría", "estado": "Estado"}
        widget={'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        
        self.fields['categoria'].empty_label = "Seleccione Categoría"

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = {'marcap','estado'}
        labels = {'marcap':"Descripcion de la Marca", "estado": "Estado"}
        widget={'marcap': forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = {'unidadp','estado'}
        labels = {'unidadp':"Descripcion de la unidad de medida", "estado": "Estado"}
        widget={'unidadp': forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

#formulario de Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'unidad', \
                  'subcategoria', 'marca', 'estado']
        exclude = {'um', 'fm', 'uc', 'fc'}
        
        widget={'descripcion': forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    

