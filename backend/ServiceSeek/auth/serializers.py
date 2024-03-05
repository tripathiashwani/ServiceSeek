from rest_framework import serializers
from .models import Product,Category,Brand,Productline

class CategorySerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source="name")
    class Meta:
        model=Category
        fields=["category_name"]
        
