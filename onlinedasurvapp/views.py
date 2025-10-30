from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'onlinedasurvapp/index.html')

def navbar(request):
    return render(request, 'onlinedasurvapp/navbar.html')

def home(request):
    return render(request, 'onlinedasurvapp/home.html')

def shop(request):
    return render(request, 'onlinedasurvapp/shopitems.html')