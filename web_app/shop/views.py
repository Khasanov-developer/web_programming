from django.shortcuts import render
from datetime import datetime
from .forms import SubscriberForm


# Create your views here.
def index(request):
    name = 'Radmir!'
    current_day = datetime.today()
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        form.save()

    return render(request, 'mainPage.html', locals())
