from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def amf(request):
    return render(request, 'amf.html')

def amo(request):
    return render(request, 'amo.html')

def contact(request):
    return render(request, 'contact.html')