from django.urls import path
from . import views

urlpatterns = [
    path('greeting', views.index, name='index'),
]