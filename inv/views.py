from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from sisfya .views import SinPrivilegios
#modulo de categorias#
class CategoriaView(SinPrivilegios, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_categoria"
    

class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
   
    model = Categoria
    template_name= "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    success_message="Categoria creada exitosamente"
    permission_required = "inv.add_categoria"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
        
class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Categoria
    template_name= "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    success_message="Categoria actualizada correctamente"
    permission_required = "inv.change_categoria"
    

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SinPrivilegios, generic.DeleteView):
   
    model = Categoria
    template_name= "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    success_message="Categoria eliminada correctamente"
    permission_required = "inv.delete_categoria"

#Modulo de Subcategorias#

class SubCategoriaView(SinPrivilegios, generic.ListView):
    
    model = SubCategoria
    template_name= "inv/subcategoria_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_subcategoria"
   


class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    
    model = SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.add_subcategoria"
  

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(SinPrivilegios, generic.UpdateView):
    model = SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.change_subcategoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name= "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.delete_subcategoria"

# modulo de marcas#
class MarcaView(SinPrivilegios, generic.ListView):
    
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_marca"
   

class MarcaNew(SinPrivilegios, generic.CreateView):
    model = Marca
    template_name= "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    permission_required = "inv.add_marca"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SinPrivilegios, generic.UpdateView):
    model = Marca
    template_name= "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    permission_required = "inv.change_marca"


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='sisfya:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto ={}
    template_name= "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method=="GET":
        contexto={'obj':marca}
    
    if request.method=="POST":
        marca.estado=False
        marca.save()
        messages.success(request, 'Marca inactivada exitosamente.')
        return redirect("inv:marca_list")

    return render(request,template_name,contexto)

class UnidadMedidaView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/unidad_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_marca"
    

class UnidadMedidaNew(SinPrivilegios, generic.CreateView):
    model = UnidadMedida
    template_name= "inv/unidad_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url=reverse_lazy("inv:unidad_list")
    permission_required = "inv.add_marca"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UnidadMedidaEdit(SinPrivilegios, generic.UpdateView):
    model = UnidadMedida
    template_name= "inv/unidad_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url=reverse_lazy("inv:unidad_list")
    permission_required = "inv.change_marca"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidad', login_url='sisfya:sin_privilegios')
def unidad_inactivar(request, id):
    unidad = UnidadMedida.objects.filter(pk=id).first()
    contexto ={}
    template_name= "inv/catalogos_del.html"

    if not unidad:
        return redirect("inv:unidad_list")

    if request.method=="GET":
        contexto={'obj':unidad}
    
    if request.method=="POST":
        unidad.estado=False
        unidad.save()
        return redirect("inv:unidad_list")

    return render(request,template_name,contexto)


#Vista de producto.

class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    permission_required="inv.view_producto"

class ProductoNew(SinPrivilegios, generic.CreateView):
    model = Producto
    template_name= "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    permission_required="inv.add_producto"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SinPrivilegios, generic.UpdateView):
    model = Producto
    template_name= "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    permission_required="inv.change_producto"
    

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='sisfya:sin_privilegios')
def producto_inactivar(request, id):
    prod=Producto.objects.filter(pk=id).first()
    contexto={}
    template_name= "inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method=="GET":
        contexto={'obj':prod}
    
    if request.method=="POST":
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")

    return render(request,template_name,contexto)

