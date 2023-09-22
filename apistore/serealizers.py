from rest_framework import serializers
from .models import Employe, Article, Sale, SaleDet, Purchase, PurchaseDet

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
        
class SaleDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDet
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
class PurchaseDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDet
        fields = '__all__'

