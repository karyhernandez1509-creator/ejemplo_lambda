from django.urls import path
from .views import productos_view

urlpatterns = [
    path('', productos_view, name='productos'),
]