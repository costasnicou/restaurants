from django.urls import path
from . import views

app_name='food'

urlpatterns = [
   
    path("<int:restaurant_id>",views.restaurant_details,name="restaurant_details"),
    # path("menu/<int:category_id>",views.menu_details,name="menu_details"),
]