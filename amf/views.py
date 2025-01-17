from django.shortcuts import render
import os
from django.conf import settings

def amf(request):
    return render(request, 'amf.html')

def fbph(request):
    # yung pOST yan yung method sa form mo. kinuha niya na yung data sa form mo
    if request.method == 'POST':
        SYN = request.POST.get('SYN')
        PHILAWYS = request.POST.get('PHILAWYS')
        FB100 = request.POST.get('FB100')
        FB180 = request.POST.get('FB180')
        FB300 = request.POST.get('FB300')
        FB390 = request.POST.get('FB390')
        CIG = request.POST.get('CIG')
        
        return render(request, 'amf/preview.html', {'SYN': SYN, 'PHILAWYS' : PHILAWYS, 'FB100' : FB100, 'FB180' : FB180, 'FB300' : FB300, 'FB390' : FB390, 'CIG' : CIG})
    return render(request, 'amf/fbph.html')

def taf(request):
    return render(request, 'amf/taf.html')

def sigmet(request):
    return render(request, 'amf/sigmet.html')

def others(request):
    return render(request, 'amf/others.html')
