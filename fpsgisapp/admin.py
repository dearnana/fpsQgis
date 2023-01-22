from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Register your models here.

from fpsgisapp.models import WaterConsumption,BetaGroup,BiPySoLegal2012,CLIENTSUS,FISPUN,Clientsnonus

class WaterConsumptionAdmin(LeafletGeoAdmin):
    pass


admin.site.register((WaterConsumption, BetaGroup, BiPySoLegal2012, CLIENTSUS, FISPUN,Clientsnonus))

df_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\waterwatch_clean2.xlsx')
#print(df_excelReader.head())

for index, row in df_excelReader.iterrows():
    Id = index
    Suburb = row['Suburb']
    NoOfSingleResProp = row['Number of single-residential properties_number']
    AvgMonthlyKL = row['Oct 2017\nkl/month']
    AvgMonthlyKLPredicted = 0
    PredictionAccuracy = 0
    Month = row['Month']
    Year = row['Year']
    DateTime = datetime.now()
    Longitude = row['Longitude']
    Latitude = row['Latitude']

    WaterConsumption(Id=Id, Suburb=Suburb, NoOfSingleResProp=NoOfSingleResProp,
                     AvgMonthlyKL=AvgMonthlyKL, AvgMonthlyKLPredicted=AvgMonthlyKLPredicted,
                     PredictionAccuracy=PredictionAccuracy, Month=Month, Year=Year,
                     DateTime=DateTime, geom=Point(Longitude, Latitude)).save()


""" **********models for fps begins here*********** """


BetaGroup_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\betagroup.xlsx')
#print(df_excelReader.head())

for index, row in BetaGroup_excelReader.iterrows():
    Id = index
    EINN = row['EINN']
    beta_testersfor_GSOC = row['beta_testersfor_GSOC']
    address = row['address']
    street = row['street']
    location = row['location']
    contact_person = row['contact_person']
    email_address = row['email_address']
    phone_number = row['phone_number']
    smaller_unit = row['smaller_unit']
    city_unit = row['city_unit']
    unit_country = row['unit_country']
    organisation_url = row['organisation_url']
    latitude = row['latitude']
    longitude = row['longitude']


    BetaGroup(Id=Id, EINN=EINN, beta_testersfor_GSOC=beta_testersfor_GSOC,
                     address=address, street=street,
                     location=location, contact_person=contact_person, email_address=email_address,
                     phone_number=phone_number, smaller_unit=smaller_unit, city_unit=city_unit, unit_country=unit_country,
                     organisation_url=organisation_url, geom=Point(latitude, longitude)).save()


BiPySoLegal2012_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\BiPySoLegal2012.xlsx')
#print(BiPySoLegal2012_excelReader.head())

for index, row in BiPySoLegal2012_excelReader.iterrows():
    Id = index
    nation = row['nation']
    CAMEO = row['CAMEO']
    Threedigit = row['Threedigit']
    net = row['net']
    BioPsySoci = row['BioPsySoci']
    Legal = row['Legal']
    Unk = row['Unk']

    BiPySoLegal2012(Id=Id, nation=nation, CAMEO=CAMEO,
                     Threedigit=Threedigit, net=net,
                     BioPsySoci=BioPsySoci, Legal=Legal, Unk=Unk).save()


CLIENTSUS_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\CLIENTSUS.xlsx')
#print(df_excelReader.head())

for index, row in CLIENTSUS_excelReader.iterrows():
    Id = index
    EINN = row['EINN']
    organ = row['organ']
    contact = row['contact']
    phone = row['phone']
    email = row['email']
    address = row['address']
    city = row['city']
    zipcode = row['zipcode']
    country = row['country']
    latitude = row['latitude']
    longitude = row['longitude']


    CLIENTSUS(Id=Id, EINN=EINN, organ=organ,
                     contact=contact, phone=phone,
                     email=email, address=address, city=city,
                     zipcode=zipcode, country=country, geom=Point(latitude, longitude)).save()



FISPUN_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\FISPUN.xlsx')
#print(FISPUN_excelReader.head())

for index, row in FISPUN_excelReader.iterrows():
    Id = index
    nation = row['nation']
    CAMEO = row['CAMEO']
    FIPS = row['FIPS']
    UN = row['UN']
    Threedigit = row['Threedigit']


    FISPUN(Id=Id, nation=nation, CAMEO=CAMEO,
                     FIPS=FIPS, UN=UN, Threedigit=Threedigit).save()



Clientsnonus_excelReader = pd.read_excel(r'C:\Users\dearn\Desktop\fpsProject\v5\vgsoc\Clientsnonus.xlsx')
#print(Clientsnonus_excelReader.head())

for index, row in Clientsnonus_excelReader.iterrows():
    Id = index
    EIN_us_affiliate = row['EIN_us_affiliate']
    name_of_organization = row['name_of_organization']
    contact_in_country = row['contact_in_country']
    phone = row['phone']
    email = row['email']
    city = row['city']
    country = row['country']
    latitude = row['latitude']
    longitude = row['longitude']


    Clientsnonus(Id=Id, EIN_us_affiliate=EIN_us_affiliate, name_of_organization=name_of_organization,
                     contact_in_country=contact_in_country, phone=phone,
                     email=email, city=city,
                     country=country, geom=Point(latitude, longitude)).save()