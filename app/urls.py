from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('',include(('sisfya.urls','sisfya'), namespace='sisfya')),
    path('inv/',include(('inv.urls','inv'), namespace='inv')),
    path('cmp/',include(('cmp.urls','cmp'), namespace='cmp')),
    path('fac/', include(('fac.urls','fac'),namespace='fac')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    
    
    
    
    path('admin/', admin.site.urls),
]

