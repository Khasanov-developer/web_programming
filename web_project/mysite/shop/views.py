from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):

    return render(request, 'shop/index.html', locals())