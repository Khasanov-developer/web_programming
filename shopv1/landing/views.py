from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from products.models import Product, ProductImage

# Create your views here.
def landing(request):
    form = SubcriberForm(request.POST or None)

    if request.method=="POST":
        print(form)
        form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())