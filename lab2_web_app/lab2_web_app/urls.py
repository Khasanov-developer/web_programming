from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    # when client request http://127.0.0.1:8000/index/, the project will find the mapped process method in my_hello_world app's urls.py file.
    path('index/', include('hello_world_app.urls'))
]