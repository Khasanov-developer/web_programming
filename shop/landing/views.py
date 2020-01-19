from django.shortcuts import render, redirect
from .forms import SubscriberForm
from products.models import *
from django.http import JsonResponse


def landing(request):
    name = "Khasss"
    current_day = "08.12.2019"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    session_key = request.session.session_key
    if 'city' in request.COOKIES.keys():
        print('in ifcoockie')
        city_name = request.COOKIES.get('city')
        print(city_name)
        products_images = ProductImage.objects.filter(product__city = city_name, is_active=True, is_main=True, product__is_active=True)
        products_images_phones = products_images.filter(product__category__id=1)
        products_images_laptops = products_images.filter(product__category__id=2)
    else:
        print('not in if')
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
        products_images_phones = products_images.filter(product__category__id=1)
        products_images_laptops = products_images.filter(product__category__id=2)
    if not session_key:
        request.session.cycle_key()

    return render(request, 'landing/home.html', locals())
