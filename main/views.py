from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def products(request):
    return render(request, 'main/products.html')


def prices(request):
    return render(request, 'main/prices.html')


def contact(request):
    return render(request, 'main/contact.html')