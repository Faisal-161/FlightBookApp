import django_filters
from bookflightapp.models import *
from django import forms
from django_filters import *
    
class DateInput(forms.DateTimeInput):
  input_type ='date'


class FlightFilter(django_filters.FilterSet):
    departure_datetime = DateTimeFilter()
    arrival_datetime = DateTimeFilter()
    
    class Meta:
        model = Flight
        fields = ["aeroplane","departure","destination","price","departure_datetime","arrival_datetime"]
        

class PassengerFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ["passenger_first_name","passenger_last_name"]
        

        