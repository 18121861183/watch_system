"""watch_system URL Configuration

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
from django.contrib import admin
from django.urls import path

from agriculture import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('edit/', views.web_edit),
    path('web_detail/', views.web_detail),
    path('inte_list/', views.intel_list),
    path('intelligence_record/', views.intelligence_record),
    path('import/', views.import_intel),
    path('edit_detail/', views.edit_web_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

