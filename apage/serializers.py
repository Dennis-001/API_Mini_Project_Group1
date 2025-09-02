from rest_framework import serializers
from .models import Product,cartd

class produceSerializer(serializers.ModelSerializer):
     class Meta:
          model=Product
          fields='_all_'
class cartSerializer(serializers.ModelSerializer):
     class Meta:
          model=cartd
          fields='_all_'

