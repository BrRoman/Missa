from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('missa/', include('apps.main.urls')),
    path('missa/admin/', admin.site.urls),
]
