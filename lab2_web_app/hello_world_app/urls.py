from django.urls import path
# import views from local directory.
from . import views
urlpatterns = [
    # When user request home page http://localhost:8000/hello_world_app, it will invoke the home function defined in views.py.
    path('', views.index_page, name='index'),
]
