from django.shortcuts import render, HttpResponse
from datetime import datetime
from .forms import SubscriberForm
from products.models import *

# Create your views here.
def index(request):

    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        name = data['name']
        email = data['email']
        form.save()
        # return render(request, 'shop/request.html', locals())

    return render(request, 'shop/mainPage.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'shop/home.html', locals())
