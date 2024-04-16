from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    with open('taf_analyst/output.txt', 'r') as file:
        txt_content = file.read()
    return render(request, 'home.html', {'txt_content': txt_content})

def about(request):
    return render(request, 'about.html')

def amf(request):
    return render(request, 'amf.html')

def amo(request):
    return render(request, 'amo.html')

def contact(request):
    return render(request, 'contact.html')

# def compare_taf(request):
#     # Call your script's main function
#     result = main_function()

#     # You can process 'result' as needed and pass it to the template
#     return render(request, 'home.html', {'result': result})

