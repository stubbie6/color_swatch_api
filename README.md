# color_swatch_api

Django Color Swatch API
Has one main GET request: http://localhost:8000/generateSwatch

In addition to installing django you'll also need to install the following:

CORS-headers : python -m pip install django-cors-headers
TastyPie     : pip install django-tastypie

Example response:

[
    {
        "color_type": "RGB",
        "RGB": "#73660b",
        "Hue": 52.5,
        "Saturation": 82.54,
        "Lightness": 24.71
    },
    {
        "color_type": "RGB",
        "RGB": "#a23c7d",
        "Hue": 321.76,
        "Saturation": 45.95,
        "Lightness": 43.53
    },
    {
        "color_type": "HSL",
        "RGB": "#cb1bea",
        "Hue": 291.01,
        "Saturation": 83.13,
        "Lightness": 51.18
    },
    {
        "color_type": "HSL",
        "RGB": "#b1b95b",
        "Hue": 65.11,
        "Saturation": 40.17,
        "Lightness": 54.12
    },
    {
        "color_type": "RGB",
        "RGB": "#a05cc9",
        "Hue": 277.43,
        "Saturation": 50.23,
        "Lightness": 57.45
    }
]
