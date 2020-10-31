from django.urls import path
from django.contrib.auth import views as auth_views
from sisfya.views import Home, HomeSinPrivilegios
from sisfya import views



urlpatterns = [
    path('',views.index, name='index'), 
    path('home/' ,Home.as_view(), name='home'), 
    path('login/',auth_views.LoginView.as_view(template_name='sisfya/login.html'),
        name='login'), 
    path('logout/',auth_views.LogoutView.as_view(template_name='sisfya/login.html'),
        name='logout'),
    path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]