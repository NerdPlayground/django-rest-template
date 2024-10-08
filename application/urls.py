"""
URL configuration for application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from decouple import config
from django.conf import settings
from django.contrib import admin
from django.urls import path,reverse
from django.http import HttpResponsePermanentRedirect
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

def home(request):
    return HttpResponsePermanentRedirect(reverse("swagger-ui"))

ADMIN_SITE_URL="{}/".format(config('ADMIN_SITE_URL'))
VERSION=settings.VERSION.split(".")[0]
URL_HEADER=f"application-api/v{VERSION}"

urlpatterns = [
    path("",home,name="home"),
    path(ADMIN_SITE_URL,admin.site.urls),
    path(f"{URL_HEADER}/schema/",SpectacularAPIView.as_view(),name="schema"),
    path(f"{URL_HEADER}/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui"),
]
