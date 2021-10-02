from django.urls import path

from rest_framework import routers
from .views import ProductView


router = routers.SimpleRouter()

router.register('products', ProductView, basename='products')


urlpatterns = []
urlpatterns += router.urls