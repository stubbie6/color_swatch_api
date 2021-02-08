# api/resources.py
from tastypie.resources import ModelResource
from api.models import Rgb
from api.models import Hsl
from api.models import Brgb
from api.models import ColorSpecsCollection
from api.models import ColorSpecs
from tastypie.authorization import Authorization

class RgbResource(ModelResource):
    class Meta:
        queryset = Rgb.objects.all()
        resource_name = 'RGB'
        authorization = Authorization()

class HslResource(ModelResource):
    class Meta:
        queryset = Hsl.objects.all()
        resource_name = 'HSL'
        authorization = Authorization()

class BrgbResource(ModelResource):
    class Meta:
        queryset = Brgb.objects.all()
        resource_name = 'BRGB'
        authorization = Authorization()

class ColorSpecsCollectionResource(ModelResource):
    class Meta:
        queryset = ColorSpecsCollection.objects.all()
        resource_name = 'COLOR_SPECS_COLLECTION'
        authorization = Authorization()

class ColorSpecsResource(ModelResource):
    class Meta:
        queryset = ColorSpecs.objects.all()
        resource_name = 'COLOR_SPECS'
        authorization = Authorization()

