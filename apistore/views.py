
from rest_framework import generics
from .models import Employe, Article, Sale, SaleDet, Purchase, PurchaseDet
from .serealizers import EmployeSerializer, ArticleSerializer, SaleSerializer, SaleDetSerializer, PurchaseSerializer, PurchaseDetSerializer

class EmployeListCreateView(generics.ListCreateAPIView):
    queryset = Employe.objects.all()    
    serializer_class = EmployeSerializer

class EmployeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
class SaleDetListCreateView(generics.ListCreateAPIView):
    queryset = SaleDet.objects.all()
    serializer_class = SaleDetSerializer

class SaleDetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleDet.objects.all()
    serializer_class = SaleDetSerializer

class PurchaseListCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseDet.objects.all()
    serializer_class = PurchaseDetSerializer

class PurchaseDetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseDet.objects.all()
    serializer_class = PurchaseDetSerializer
    

   
