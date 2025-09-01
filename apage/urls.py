from django.urls import path
from . import views

urlpatterns=[
       path('/home',views.home,name='home'),
       path('/produce',views.produce,name='produce'),
       path('/cart',views.cart,name='cart'),
       path('/checkout',views.checkout,name='checkout'),
]
