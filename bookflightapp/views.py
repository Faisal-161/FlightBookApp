from django.shortcuts import render
from .forms import *
from .models import Flight
from bookflightapp.filter import FlightFilter, PassengerFilter
from bookflightapp.choices import country_choices
from datetime import datetime


def index(request):

  return render(request,'bookflightapp/index.html')

def search_by_name(request):
  flight=Flight.objects.all().order_by("-departure_datetime").exclude(departure_datetime__lte="2020-3-3")

  context={
    'flight':flight,
    'country_choices':country_choices
  }
  
  #departure
  if 'departure' in request.GET:
    departure=request.GET['departure']
    if departure:
      flight=Flight.objects.filter(departure__country__iexact=departure)

  #destination
  if 'destination' in request.GET:
    destination=request.GET['destination']
    if destination:
      flight=Flight.objects.filter(destination__country__iexact=destination)
  
  #departure-date

  context={
    'flight':flight,
    'country_choices':country_choices
  }

  return render(request,'bookflightapp/namesearch.html',context)
  
def search_by_date(request):

  flight=Flight.objects.all().order_by("-departure_datetime").exclude(departure_datetime__lte="2020-3-3")

  context={
    'flight':flight,
    'country_choices':country_choices
  }

  if 'departure-date' in request.GET:

    departure_date=request.GET['departure-date']

    if departure_date: 
      flight=Flight.objects.filter(departure_datetime__gte=departure_date)
  
  #arrival-date
  if 'arrival-date' in request.GET:

    arrival_date=request.GET['arrival-date']
    if arrival_date:
      flight=Flight.objects.filter(arrival_datetime__lt=arrival_date)

  context={
    'flight':flight,
    'country_choices':country_choices
  }

  return render(request,'bookflightapp/datesearch.html',context)


    

def booking_form(request):
  pass

def flight_detail_id(request):
  pass