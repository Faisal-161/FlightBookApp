from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='index'),
  path('namesearch',views.search_by_name,name='name-search'),
  path('datesearch',views.search_by_date,name='date-search'),
  path("book_form/",views.booking_form,name="Book_form"),
  path("flight/<str:id>/",views.flight_detail_id,name="bookdetails"),
]