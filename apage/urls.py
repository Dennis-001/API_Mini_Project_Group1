from django.urls import path
from . import views

  urlpatterns=[
       path('',views.home,name=home),
       path('',views.produce,name=produce),
       path('',views.cart,name=cart),
       path('',views.checkout,name=checkout),
]
