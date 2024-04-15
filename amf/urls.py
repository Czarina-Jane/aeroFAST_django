from django.urls import path
# pinalitan ko ng * para lahat pre ng nasa views.py mo macall mo dito

from .views import * # Add home function from views

urlpatterns = [    
    # Add path from local views
    path('amf/', amf, name='amf'), 
    path('amf/taf/', taf, name='taf'), 
    path('amf/sigmet/', sigmet, name='sigmet'),
    path('amf/others/', others, name='others'),  
    path('amf/fbph', fbph, name='fbph'),
]