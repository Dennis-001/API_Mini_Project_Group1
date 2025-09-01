from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Product
# Create your views here.
def home(request):
    products=Product.objects.all()
    serializer=ProductSerrializer(products,many=TRUE)
    template=loader.get_template('wpage.html')
    context={'products':products,}
    return HttpResponse(template.render(context,request))
def produce(request):
      return render(request,"ppage.html")
def cart(request):
      cproducts=cartd.objects.all()
      serializer=cartdserializer(cproducts,many=TRUE)
      template=loader.get_template('cpage.html')
      context={'cartd':cartd,}
      return HttpResponse(template,render,(context,request))
def checkout(request):
      cartd=cartd.objects.all()
      return(request,'chpage.html',{{'cartd:cartd'}})
