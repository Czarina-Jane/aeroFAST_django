from django.urls import path
from .views import *

urlpatterns = [    
    # Add path from local views
    path('', home, name='home'), 
    # path('', compare_taf, name='compare_taf'), 

    path('about/', about, name='about'), 
    path('amf/', amf, name='amf'), 
    path('amo/', amo, name='amo'),
    path('contact/', contact, name='contact'),  
]