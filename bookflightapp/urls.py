from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='index'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('createflight',views.create_flight,name='create-flight'),
  path('signup',views.signup,name='signup'),
  path('namesearch',views.search_by_name,name='name-search'),
  path('datesearch',views.search_by_date,name='date-search'),
  path("bookflight/",views.book_flight,name="book-flight"),
  path("flight/<str:pk>/",views.flight_detail,name="bookdetails"),
]