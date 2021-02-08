from django.shortcuts import render
from django.http import JsonResponse
from random import randint
from colorsys import rgb_to_hls

# send 5 random color swatches
def generateSwatch(request):
     
    numSwatches = 5
    swatch_data = []
    
    for x in range(numSwatches):
        random_rgb = generateRGB()
        #Generate HSV Equivalent
        hsv_equiv = rgb_to_hls((random_rgb[1] / 255),(random_rgb[2] / 255),(random_rgb[3] / 255))
        #Populate Color Data - HSL to 2 sig digits otherwise the conversion back to RGB can be off
        color_data =  {'color_type': colorType(), 'RGB': random_rgb[0], "Hue": round(hsv_equiv[0]*360,2), "Saturation" : round(hsv_equiv[2]*100,2), "Lightness" : round(hsv_equiv[1]*100,2) }
        swatch_data.append(color_data)               
    return JsonResponse(swatch_data, safe=False)

# randomly determine the color type
def colorType():
    value = randint(0, 1)
    if (value == 1):
        return "HSL"
    else:
        return "RGB"   

# randomly generate a color in RGB
def generateRGB():
    red_value = randint(0,255)
    green_value = randint(0,255)
    blue_value = randint(0,255)
    rgb_hash = '#%02x%02x%02x' % (red_value, green_value, blue_value)
    return (rgb_hash, red_value, green_value, blue_value)
 
