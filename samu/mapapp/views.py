from django.shortcuts import render

def home(request):
    return render(request, 'chennai.html')

def eg(request):
    return render(request, 'Egmore.html')

def koyam(request):
    return render(request, 'koyambedu.html')

def nungu(request):
    return render(request, 'Nungambakkam.html')

def virug(request):
    return render(request, 'virugambakkam.html')