from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# def home(request):
#     products = Product.objects.all().order_by('name')

#     context = {
#         'products': products
#     }
#     return render(request, 'mainpage/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'mainpage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['products'] = Product.objects.all().order_by('name')
        return context

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainpage/detail.html'