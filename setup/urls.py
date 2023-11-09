from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('galeria.urls')), # Rota do projeto galeria
    path('', include('usuarios.urls')) # Rota do projeto usuarios
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
