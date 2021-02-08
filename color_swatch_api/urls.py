"""color_swatch_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from api.resources import RgbResource
from api.resources import HslResource
from api.resources import BrgbResource
from api.resources import ColorSpecsCollectionResource
from api.resources import ColorSpecsResource
from api.views import generateSwatch

rgb_resource = RgbResource()
hsl_resource = HslResource()
brgb_resource = BrgbResource()
color_specs_collection = ColorSpecsCollectionResource()
color_specs = ColorSpecsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('rgb/', include('rgb_resource.urls')),
    url(r'^rgb/', include(rgb_resource.urls)),
    url(r'^hsl/', include(hsl_resource.urls)),
    url(r'^brgb/', include(brgb_resource.urls)),
    url(r'^color-spec/', include(color_specs.urls)),
    url(r'^color-spec-collection/', include(color_specs_collection.urls)),
    path('generateSwatch/', generateSwatch, name='generateSwatch'),
]
