"""api1django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EmployeListCreateView, EmployeDetailView, ArticleDetailView, ArticleListCreateView,SaleDetailView, SaleListCreateView, SaleDetListCreateView,SaleDetDetailView ,PurchaseListCreateView, PurchaseDetDetailView, PurchaseDetListCreateView, PurchaseDetailView
urlpatterns = [
    path('employes/', EmployeListCreateView.as_view(), name='employe-list'),
    path('employes/<int:pk>/', EmployeDetailView.as_view(), name='employe-detail'),
    
    path('articles/',ArticleListCreateView.as_view(), name='employe-list'),
    path('articles/<int:pk>/',ArticleDetailView.as_view(), name='employe-detail'),
    
    path('sales/', SaleListCreateView.as_view(), name='employe-list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='employe-detail'),
    
    path('saledets/', SaleDetListCreateView.as_view(), name='employe-list'),
    path('saledets/<int:pk>/', SaleDetDetailView.as_view(), name='employe-detail'),
    
    path('purchases/', PurchaseListCreateView.as_view(), name='employe-list'),
    path('purchases/<int:pk>/',PurchaseDetailView.as_view(), name='employe-detail'),  
    
    path('purchasedets/', PurchaseDetListCreateView.as_view(), name='employe-list'),
    path('purchasedets/<int:pk>/', PurchaseDetDetailView.as_view(), name='-detail'),
]