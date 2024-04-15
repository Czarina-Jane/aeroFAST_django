from django.shortcuts import render

def amf(request):
    return render(request, 'amf.html')

def fbph(request):
    # yung pOST yan yung method sa form mo. kinuha niya na yung data sa form mo
    if request.method == 'POST':
        SYN = request.POST.get('SYN')
        PHILAWYS = request.POST.get('PHILAWYS')
        #  test lang sa terminal kung may nakukuha na data. pwede idelete
        print("SYN:", SYN)
        print("PHILAWYS:", PHILAWYS)
        # nilagay lang sa array yung data para ito yung icall sa preview.html
        return render(request, 'preview.html', {'SYN': SYN, 'PHILAWYS': PHILAWYS})
    return render(request, 'amf/fbph.html')

def taf(request):
    return render(request, 'amf/taf.html')

def sigmet(request):
    return render(request, 'amf/sigmet.html')

def others(request):
    return render(request, 'amf/others.html')
