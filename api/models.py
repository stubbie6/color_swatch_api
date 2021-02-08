from django.db import models
from django.core.validators import MaxValueValidator
from random import *
# define color space types
# RGB
class Rgb(models.Model):
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
def __str__(self):
        return '%s %s %s' % (self.red, self.green, self.blue)
# HSL    
class Hsl(models.Model):
    hue = models.IntegerField(default=0)
    saturation = models.IntegerField(default=0)
    lightness = models.IntegerField(default=0)

# BRGB
class Brgb(models.Model):
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)

class ColorSpecsCollection(models.Model):
    collection_size = models.IntegerField(default=0)

class ColorSpecs(models.Model):
    RGB = 'RGB'
    HSL = 'HSL'
    BRGB = 'BRGB'
    COLOR_TYPE_CHOICES = [
        (RGB, 'RGB'), (HSL, 'HSL'), (BRGB, 'BRGB'),
    ]

    color_type = models.CharField(
        max_length = 4,
        choices = COLOR_TYPE_CHOICES,
        default=RGB,
    )
    red = models.IntegerField(default=0, null=True, blank=True)
    green = models.IntegerField(default=0, null=True, blank=True)
    blue = models.IntegerField(default=0, null=True, blank=True)
    hue = models.IntegerField(default=0, null=True, blank=True)
    saturation = models.IntegerField(default=0, null=True, blank=True)
    lightness = models.IntegerField(default=0, null=True, blank=True)
    brgb_red = models.IntegerField(default=0, null=True, blank=True)
    brgb_green = models.IntegerField(default=0, null=True, blank=True)
    brgb_blue = models.IntegerField(default=0, null=True, blank=True)
    color_specs_collection = models.ForeignKey(ColorSpecsCollection, on_delete=models.CASCADE, null=True, blank=True)

# Better ways to do it, but couldn't (quickly) figure out how to get them to work

# Validation on the RGB values
#    red = models.PositiveIntegerField(validators=[MaxValueValidator(255)])
#    green = models.PositiveIntegerField(validators=[MaxValueValidator(255)])
#    blue = models.PositiveIntegerField(validators=[MaxValueValidator(255)])

# Enum for Color Types
#class Color(Enum):
#    RGB = "RGB"
#    HSL = "HSL"
#    BRGB = "BRGB"




