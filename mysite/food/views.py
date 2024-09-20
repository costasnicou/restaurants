from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Restaurant, MenuCategory,MenuItem,City
# Create your views here.


# index route on url localhost

# show 3 featured restaurants in homepage

def index(request):
    restaurants = Restaurant.objects.filter(restaurant_featured=True)
    return render(request,"food/index.html",{
        "restaurants":restaurants
    })


# restaurant_details
def restaurant_details(request,restaurant_slug):
    restaurants = Restaurant.objects.filter(restaurant_featured=True)
    restaurant = get_object_or_404(Restaurant, restaurant_slug=restaurant_slug)
    restaurant_imgs = restaurant.restaurant_imgs.all()
    menu_categories = restaurant.menu_categories.all()
    social_icons = restaurant.social_icons.all()
    google_maps_api_key = "AIzaSyCDQPDmTsqHlLzzFQM-FugRBB8fTDT2644" 
    return render(request,"food/restaurant-details.html",{
        "feautured_restaurants":restaurants,
        "restaurant_imgs": restaurant_imgs,
        "social_icons":social_icons,
        "restaurant":restaurant,
        "menu_categories":menu_categories,
        'google_maps_api_key': google_maps_api_key,
    })


# list of all restaurants
def restaurant_list(request):
    cities = City.objects.all()
    restaurants = Restaurant.objects.all()
    return render(request,"food/restaurants_list.html",{
        "cities":cities,
        "restaurants":restaurants
    })


# restaurants by city
def restaurants_by_city(request,city_slug):
    cities = City.objects.all()
    city = get_object_or_404(City, city_slug=city_slug)
    filtered_restaurants = city.restaurant_by_city.all()
    return render(request,"food/restaurants_by_city.html",{
        "cities": cities,
        "city":city,
        "filtered_restaurants":filtered_restaurants,
    })
    

def menu_list(request,menu_slug,restaurant_slug):

    # i need to grub the menu categories for that specific restaurant

    restaurant = get_object_or_404(Restaurant, restaurant_slug=restaurant_slug)
    menu_categories = restaurant.menu_categories.all()

    menu_category = get_object_or_404(MenuCategory, menu_slug=menu_slug)
    menu_items = menu_category.menu_items.all()
    return render(request,"food/menu_list.html",{
        "restaurant":restaurant,
        "menu_categories": menu_categories,
        "menu_category":menu_category,
        "menu_items":menu_items,
    })

    