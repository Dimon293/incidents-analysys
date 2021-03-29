"""dtp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from transport.views import color_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', color_page),
    path('api/transport/', include('transport.urls')),
    path('api/participant/', include('participant.urls')),
    path('api/incident/', include('incident.urls')),
]

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
