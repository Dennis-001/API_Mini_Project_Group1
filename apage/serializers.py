from rest_framework import serializers
from .models import produce,cart

 class produceSerializer(serializer.ModelSerializer):
     class Meta:
          model=produce
          fields='_all_'
 class cartSerializer(serializer.ModelSerializer):
     class Meta:
          model=cart
          fields='_all_'

