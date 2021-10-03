from django.urls import path
from .views import ProductListView, ProductDetailView, StoreListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('store/', StoreListView.as_view(), name='store'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]