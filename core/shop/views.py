from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
# Create your views here.
class ShopProductGridViews(TemplateView):
    template_name = 'shop/product-grid.html'