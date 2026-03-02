
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def About_us(request):
    return render(request, 'main/About_us.html')

def Analytic(request):
    return render(request, 'main/Analytic.html')

def connect(request):
    return render(request, 'main/connect.html')

def Design(request):
    return render(request, 'main/Design.html')

def Finance(request):
    return render(request, 'main/Finance.html')

def Log_in(request):
    return render(request, 'main/Log_in.html')

def main(request):
    return render(request, 'main/main.html')

def Managing(request):
    return render(request, 'main/Managing.html')

def Marketing(request):
    return render(request, 'main/Marketing.html')

def Programming(request):
    return render(request, 'main/Programming.html')

def Teachers(request):
    return render(request, 'main/Teachers.html')