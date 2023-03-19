from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Products, ProductCategory


# Create your views here.
class IndexView(TemplateView):
    template_name = 'products\index.html'


class ProductsView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'products\products.html'
    # paginate_by = 3
