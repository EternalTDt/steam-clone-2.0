from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'mainpage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Product.objects.all().count() > 0:
            context['products'] = Product.objects.all().order_by('name')
            return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainpage/detail.html'


class StoreListView(ListView):
    model = Product
    template_name = 'mainpage/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Product.objects.filter(product_type=1).count() > 0:
            context['products'] = Product.objects.filter(product_type=1).order_by('name')
            return context

class SoftwareListView(ListView):
    model = Product
    template_name = 'mainpage/software-soft.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Product.objects.filter(product_type=2).count() > 0:
            context['programms'] = Product.objects.filter(product_type=2).order_by('name')
            return context