"""
URL configuration for webapps2025 project.

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
from django.urls import path, include
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView


urlpatterns = [
    path('webapps2025/admin/', admin.site.urls),
    path('webapps2025/register/', include('register.urls')),
    path('webapps2025/payapp/', include('payapp.urls')),
    path('webapps2025/conversion/', include('conversion.urls')),
    path('webapps2025/', RedirectView.as_view(url=reverse_lazy('register:home'))),
    path('', RedirectView.as_view(url=reverse_lazy('register:home')))
]
