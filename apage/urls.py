from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet,CartViewSet,ProduceViewSet,AdditionViewSet,AddCartViewSet,CheckoutViewSet
router=DefaultRouter()
router.register(r'home',HomeViewSet,basename='home')
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'produce',ProduceViewSet,basename='produce')
router.register(r'produce_addittion',AdditionViewSet, basename='produce_addittion')
router.register(r'checkout',CheckoutViewSet,basename='checkout')
urlpatterns=[
       path('',include(router.urls)),

]
