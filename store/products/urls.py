from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
]
