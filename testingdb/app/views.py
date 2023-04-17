from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'accounts/login2.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forgot.html')


def staffs(request):
    return render(request,'accounts/staffs.html')


def house(request):     
    return render(request,'Enviroment/house.html')


def renter(request):

    return render(request,'Enviroment/renter.html')

def enviroment(request):

    return render(request,'Enviroment/enviroment.html')




def cleaning(request):
    return render(request,'Enviroment/cleaning.html')

def reports(request):
    return render(request,'Enviroment/reports.html')

def Payment_Method(request):
    return render(request,'Enviroment/Payment_Method.html')


def Transaction(request):
    return render(request,'Enviroment/Transaction.html')


def Reports2(request):
    return render(request,'Enviroment/Reports2.html')




