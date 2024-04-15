from django.shortcuts import render

def amf(request):
    return render(request, 'amf.html')

def fbph(request):
    return render(request, 'amf/fbph.html')

def taf(request):
    return render(request, 'amf/taf.html')

def sigmet(request):
    return render(request, 'amf/sigmet.html')

def others(request):
    return render(request, 'amf/others.html')