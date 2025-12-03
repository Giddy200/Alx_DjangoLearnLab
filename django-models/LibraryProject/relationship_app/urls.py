from django.urls import path
from . import views # Import the views from the current app's views.py

urlpatterns = [
    # path(route, view_function, name)
    path('', views.list_books, name='welcome'),
]