from django.contrib import admin
from .models import Airport,Flight,Booking


class BookManager(admin.ModelAdmin):
  list_filter=['booking_datetime']
  search_fields = ["Booking"]
  date_hierarchy = "booking_datetime"
    
class AirportManager(admin.ModelAdmin):
  search_fields = ["Airport"]
  


class FlightManager(admin.ModelAdmin):
  search_fields = ["Flight"]
  date_hierarchy = "departure_datetime"
  list_filter=['arrival_datetime','departure_datetime']




admin.site.register(Booking, BookManager)
admin.site.register(Airport, AirportManager)
admin.site.register(Flight, FlightManager)