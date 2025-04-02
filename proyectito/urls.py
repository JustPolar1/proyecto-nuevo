"""
URL configuration for proyectito project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacioncita import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_usuario/', views.add_usuario),
    path('update_email/', views.update_email),
    path('authenticate/', views.authentication),
    path('logout/', views.logout_view),
    path('', views.form),
    path('frutas', views.fruta, name='frutas'),
    path('fruteria', views.fruta_form),
    path('frutas/eliminar/<int:fruta_id>/', views.eliminar_fruta, name='eliminar_fruta'),
    path('frutas/modificar/<int:fruta_id>/', views.modificar_fruta, name='modificar_fruta'),
    path('coordinates/', views.coordinates, name='coordinates'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
