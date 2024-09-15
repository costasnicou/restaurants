from django.urls import path
from . import views

app_name='food'

urlpatterns = [
   
    path("<slug:restaurant_slug>",views.restaurant_details,name="restaurant_details"),
    path("<slug:restaurant_slug>/<slug:menu_slug>/",views.menu_list,name="menu_list"),
    path("city/<slug:city_slug>",views.restaurants_by_city,name="restaurants_by_city")
   
    
   
]