from django.urls import path
from .views import ProductListView, ProductDetailView, StoreListView, SoftwareListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('programms/', SoftwareListView.as_view(), name='programms'),
    path('store/', StoreListView.as_view(), name='store'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]