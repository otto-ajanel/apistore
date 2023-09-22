from django.db import models

class Employe(models.Model):
    idemploye = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.TextField()
    dpinumber =models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'employe'  
        
class Article(models.Model):
    idarticle = models.BigIntegerField(primary_key=True)
    articledes = models.CharField(max_length=100)
    porcentaje = models.BigIntegerField()

    class Meta:
        db_table='article'

class Sale(models.Model):
    idsale=models.BigIntegerField(primary_key=True)
    idcustomer=models.BigIntegerField()
    datesale=models.DateField()
    idemploye = models.BigIntegerField()
    nofacsale = models.CharField()
    idstate  = models.BigIntegerField()
    
    class Meta:
        db_table='sale'

class SaleDet(models.Model):
    idsaledet= models.BigIntegerField(primary_key=True)
    idsale= models.BigIntegerField()
    idarticle= models.BigIntegerField()
    unitsaledet= models.BigIntegerField()
    idpricesale=models.BigIntegerField()
    
    class Meta:
        db_table='saledet'
        
class Purchase(models.Model):
    idpurchase =models.BigIntegerField(primary_key = True)
    idwherehousenbranch = models.BigIntegerField()
    idsupplier = models.BigIntegerField()
    datepurch = models.DateField()
    idemploye = models.BigIntegerField()
    purchnofac = models.BigIntegerField()
    idState = models.BigIntegerField()
    
    class Meta:
        db_table='purchase'
        
class PurchaseDet(models.Model):
    idpurchdet = models.BigIntegerField(primary_key = True)
    idpurchase = models.BigIntegerField()
    unit = models.BigIntegerField()
    idarticle = models.BigIntegerField()
    damagedpurchdet = models.BigIntegerField()
    
    class Meta:
        db_table='purchasedet'
        
     