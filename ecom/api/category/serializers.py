from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     class Meta:     #check pic in phone
         model = Category
         fields = ('name','description')