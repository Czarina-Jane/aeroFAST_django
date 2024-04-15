from django.urls import path
from .views import home, about, amf, amo, contact # Add home function from views

urlpatterns = [    
    # Add path from local views
    path('home/', home, name='home'), 
    path('about/', about, name='about'), 
    path('amf/', amf, name='amf'), 
    path('amo/', amo, name='amo'),
    path('contact/', contact, name='contact'),  
]