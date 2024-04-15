from django.urls import path
from .views import amf, fbph, taf, sigmet, others # Add home function from views

urlpatterns = [    
    # Add path from local views
    path('amf/', amf, name='amf'), 
    path('amf/fbph/', fbph, name='fbph'), 
    path('amf/taf/', taf, name='taf'), 
    path('amf/sigmet/', sigmet, name='sigmet'),
    path('amf/others/', others, name='others'),  
]