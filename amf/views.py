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
        
        txtdir = os.path.join(settings.BASE_DIR, 'templates', 'txt')
        
        # Create the directory if it doesn't exist
        if not os.path.exists(txtdir):
            os.makedirs(txtdir)

        # Save inputs into text files
        with open(os.path.join(txtdir, 'SYN.txt'), 'w') as file:
            file.write(SYN)
        with open(os.path.join(txtdir, 'PHILAWYS.txt'), 'w') as file:
            file.write(PHILAWYS)
        with open(os.path.join(txtdir, 'FB100.txt'), 'w') as file:
            file.write(FB100)
        with open(os.path.join(txtdir, 'FB180.txt'), 'w') as file:
            file.write(FB180)
        with open(os.path.join(txtdir, 'FB300.txt'), 'w') as file:
            file.write(FB300)
        with open(os.path.join(txtdir, 'FB390.txt'), 'w') as file:
            file.write(FB390)        
        with open(os.path.join(txtdir, 'CIG.txt'), 'w') as file:
            file.write(CIG)                    

        # # nilagay lang sa array yung data para ito yung icall sa preview.html
        return render(request, 'preview.html', {'SYN': SYN, 'PHILAWYS' : PHILAWYS, 'FB100' : FB100, 'FB180' : FB180, 'FB300' : FB300, 'FB390' : FB390, 'CIG' : CIG})
    return render(request, 'amf/fbph.html')

def taf(request):
    return render(request, 'amf/taf.html')

def sigmet(request):
    return render(request, 'amf/sigmet.html')

def others(request):
    return render(request, 'amf/others.html')
