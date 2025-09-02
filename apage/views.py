from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Product,cartd
from rest_framework import viewsets
from .serializers import produceSerializer,cartSerializer
# Create your views here.
class HomeViewSet(viewsets.ViewSet):
 def home(request):
    products=Product.objects.all()
    serializer=ProductSerrializer(products,many=TRUE)
    template=loader.get_template('wpage.html')
    context={'products':products,}
    return HttpResponse(template.render(context,request))
class ProduceViewSet(viewsets.ViewSet):
 def produce(request):
      return render(request,"ppage.html")
class CartViewSet(viewsets.ViewSet):
 def cart(request):
      cproducts=cartd.objects.all()
      serializer=cartdserializer(cproducts,many=TRUE)
      template=loader.get_template('cpage.html')
      context={'cartd':cartd,}
      return HttpResponse(template,render,(context,request))
class CheckoutViewSet(viewsets.ViewSet):
 def checkout(request):
      cartd=cartd.objects.all()
      return(request,'chpage.html',{{'cartd:cartd'}})
class AdditionViewSet(viewsets.ModelViewSet):
 def produce_addittion(request):
    serializer=ProductSerializer(products,many=TRUE)
    if request.method=="POST":
       form=produce(request.POST)
       if form.isvalid():
         pname=form.cleaned_data["pname"]
         pcartegory=form.cleaned_data["pcartegory"]
         pprice=form.cleaned_data["pprice"]
         return HttpResponse("Product Added")
    else:
         form=produce()
         return render(request,"ppage.html")
class AddCartViewSet(viewsets.ModelViewSet):
 def cart_shop(request):
    serializer=cartdSerializer(cproducts,many=TRUE)
    if request.method=="POST":
      formb=cart(request.POST)
      if form.is_valid():
        pname=form.cleaned_data["pname"]
        pcartegory=form.cleaned_data["pprice"]
        return HttpResponse("Added to cart")
    else:
         formb=home()
         return render(request,"wpage.html")
