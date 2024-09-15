from typing import Any
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    )
from .models import ProductModel, ProductStatusType


class ShopProductGridViews(ListView):
    template_name = 'shop/product-grid.html'
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context