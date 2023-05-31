from django.shortcuts import render

# Create your views here.
def index(request):
    hello = 'Salut'
    return render(request, 'products/index.html')