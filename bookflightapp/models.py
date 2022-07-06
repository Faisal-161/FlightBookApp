import random
from django.db.models import Sum
from django.db import models

# Create your models here.

def difference(h1, m1, h2, m2):  
  t1 = h1 * 60 + m1
  t2 = h2 * 60 + m2

  if (t1 == t2):
    print("Both are same times")
    return
  else:
    diff = t2-t1
      
  h = (int(diff / 60)) % 24
  m = diff % 60

  return f"{h}"


def random_string():
  return str(random.randint(100000, 999999))


class Airport(models.Model):
  name=models.CharField(max_length=200,null=True)
  country=models.CharField(max_length=200,null=True)
  airport_code = models.CharField(max_length=3,blank=False)

  class Meta:
    ordering=['name']
    verbose_name_plural = 'Airports'


  def __str__(self):
    return self.name


class Flight(models.Model):
  aeroplane=models.CharField(max_length=100)
  departure=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departure')
  destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='destination')
  departure_datetime=models.DateTimeField()
  arrival_datetime= models.DateTimeField()
  max_passengers = models.IntegerField()
  price=models.IntegerField()

 
  
  @property
  def hourdiff(self):
    h1= self.arrival_datetime.hour
    m1= self.arrival_datetime.minute
    h2=self.departure_datetime.hour
    m2=self.departure_datetime.minute

    diff= difference(h1,m1,h2,m2)
  
    return f"{diff} hours"

  def __str__(self):
    return f"{self.departure.country} to {self.destination.country}"

class Booking(models.Model):
  reference_no = models.CharField(max_length=6,default=random_string,unique=True,editable=False,primary_key=True)
  passenger_first_name = models.CharField(max_length=200)
  passenger_last_name = models.CharField(max_length=200)
  flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
  booking_datetime=models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.passenger_last_name