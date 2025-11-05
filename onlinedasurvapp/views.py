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

def cart(request):
    return render(request, 'onlinedasurvapp/cart.html')

def blog(request):
    return render(request, 'onlinedasurvapp/blog.html')

def contact(request):
    return render(request, 'onlinedasurvapp/contact.html')

def signup(request):
    return render(request, 'onlinedasurvapp/signup.html')

def footer(request):
    return render(request, 'onlinedasurvapp/footer.html')

def chatbot(request):
    return render(request, 'onlinedasurvapp/chatbot.html')