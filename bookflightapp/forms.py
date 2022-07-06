from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms
from .models import *

    
class CreateUserForm(UserCreationForm):
  class Meta:
    model= User
    fields=['username','email','password1','password2']

class CreateFlightForm(ModelForm):
  class Meta:
    model = Flight
    fields='__all__'


class BookFlightForm(ModelForm):
  class Meta:
    model = Booking
    fields = ["passenger_first_name","passenger_last_name"]


