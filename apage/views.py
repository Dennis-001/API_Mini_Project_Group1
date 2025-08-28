from django.shortcuts import render,httpresponse
from django.http import JsonResponse 
# Create your views here.
    def home(request):
      products=Product.objects.all()
      return(request,'wpage.html',{{'products:products'}})
    def produce(request):
      return(request,'ppage.html')
    def cart(request):
      cartd=cartd.objects.all()
      return(request,'cpage.html',{{cartd:cartd}})
    def checkout(request):
      cartd=cartd.objects.all()
      return(request,'chpage.html',{{cartd:cartd}})
