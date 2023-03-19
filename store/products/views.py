from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Products, ProductCategory


# Create your views here.
class IndexView(TemplateView):
    template_name = 'products\index.html'


class ProductsView(ListView):
    model = Products
    template_name = 'products\products.html'

    # paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context
