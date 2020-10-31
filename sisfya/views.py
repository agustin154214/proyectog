from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# MIXIN PARA REDIRECCIONAR A LOS USUARIOS NO LOGEADOS
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'sisfya:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
           self.login_url='sisfya:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


def index(request):
    return render(request, "sisfya/index.html")

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'sisfya/home.html'
    login_url='sisfya:login'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "sisfya:login"
    template_name = "sisfya/sin_privilegios.html"


# Create your views here.

