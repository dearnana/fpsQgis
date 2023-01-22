#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class WaterConsumption(models.Model):
    Id = models.IntegerField(primary_key=True)
    Suburb = models.CharField(max_length=100)
    NoOfSingleResProp = models.IntegerField()
    AvgMonthlyKL = models.IntegerField()
    AvgMonthlyKLPredicted = models.IntegerField()
    PredictionAccuracy = models.IntegerField()
    Month = models.CharField(max_length=50)
    Year = models.IntegerField()
    DateTime = models.DateTimeField()
    geom = models.PointField()

    def __str__(self):
        return self.Suburb

    class Meta:
        verbose_name_plural = ''




""" **********models for fps begins here*********** """


class BetaGroup(models.Model):
    Id = models.IntegerField(primary_key=True)
    EINN = models.IntegerField(null=True)
    beta_testersfor_GSOC = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    street = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=500, null=True)
    contact_person = models.CharField(max_length=500, null=True)
    email_address = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=500, null=True)
    smaller_unit = models.CharField(max_length=500, null=True)
    city_unit = models.CharField(max_length=500, null=True)
    unit_country = models.CharField(max_length=500, null=True)
    organisation_url = models.CharField(max_length=500, null=True)
    geom = models.PointField()

    def __str__(self):
        return self.beta_testersfor_GSOC

    class Meta:
        verbose_name_plural = 'Beta Group'




class BiPySoLegal2012(models.Model):
    Id = models.IntegerField(primary_key=True)
    nation = models.CharField(max_length=300, null=True)
    CAMEO = models.CharField(max_length=300, null=True)
    Threedigit = models.IntegerField(null=True)
    net = models.CharField(max_length=300, null=True)
    BioPsySoci = models.FloatField(null=True)
    Legal = models.FloatField(null=True)
    Unk = models.FloatField(null=True)

    def __str__(self):
        return self.nation

    class Meta:
        verbose_name_plural = 'BiPySoLegal2012'



class CLIENTSUS(models.Model):
    Id = models.IntegerField(primary_key=True)
    EINN = models.IntegerField(null=True)
    organ = models.CharField(max_length=300,null=True)
    contact = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=300,null=True)
    email = models.CharField(max_length=300,null=True)
    address = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=300,null=True)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=300,null=True)
    geom = models.PointField()

    def __str__(self):
        return self.organ

    class Meta:
        verbose_name_plural = 'CLIENTSUS'


class FISPUN(models.Model):
    Id = models.IntegerField(primary_key=True)
    nation = models.CharField(max_length=100,null=True)
    CAMEO = models.CharField(max_length=100,null=True)
    FIPS = models.CharField(max_length=100,null=True)
    UN = models.CharField(max_length=100,null=True)
    Threedigit = models.IntegerField(null=True)

    def __str__(self):
        return self.nation

    class Meta:
        verbose_name_plural = 'FISPUN'



class Clientsnonus(models.Model):
    Id = models.IntegerField(primary_key=True)  
    EIN_us_affiliate = models.CharField(max_length=300,null=True)
    name_of_organization = models.CharField(max_length=300,null=True)
    contact_in_country = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=300,null=True)
    country = models.CharField(max_length=300,null=True)
    geom = models.PointField()

    def __str__(self):
        return self.name_of_organization

    class Meta:
        verbose_name_plural = 'Clients Non US'