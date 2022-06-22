from django.contrib import admin
from .models import Airport,Flight,Booking

flightBookModels=[Airport,Flight,Booking]

admin.site.register(flightBookModels)
# Register your models here.
