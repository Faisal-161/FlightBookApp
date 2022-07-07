from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from .models import *
from bookflightapp.choices import country_choices
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
  flight=Flight.objects.all().order_by("-departure_datetime").exclude(departure_datetime__lte="2020-3-3")

  context={
    'flight':flight
  }

  return render(request,'bookflightapp/index.html',context)

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

@login_required(login_url='login')
def book_flight(request):
  return render(request,'bookflightapp/createflight.html')

def signup(request):
  if request.user.is_authenticated:
    return redirect('index')
  else:
    form=CreateUserForm()
    if request.method == "POST":
      form=CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request, "Account was created for " + user)

        return redirect('login')

  context={'form':form}
  return render(request,'bookflightapp/signup.html',context)
    

def create_flight(request):

  return render(request,'bookflightapp/createflight.html')

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('index')
  else:
    if request.method =="POST":
      user_name= request.POST.get('username')
      password= request.POST.get('password')

      user=authenticate(request,username=user_name,password=password)
      if user is not None:
        login(request,user)
        return redirect('index')
      else:
        messages.info(request,"Username Or Password Is Incorrect")

  context = {}
    

  return render(request,'bookflightapp/login.html',context)

def flight_detail(request,pk):
  booking=Booking.objects.all()
  bookfilter=booking.filter(flight__id=pk)
  all_flights = Flight.objects.all()

  book_count=booking.count()
  flight_price=Flight.objects.get(id=pk).price

  total_price = flight_price * book_count

  item=get_object_or_404(Flight,id=pk)

  context={
    'item':item,
    'all_flight':bookfilter,
    'total_price':total_price
  }
  return render(request,'bookflightapp/flightdetail.html',context)

def logoutUser(request):
  logout(request)
  return redirect('login')
  