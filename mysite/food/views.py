from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Restaurant, MenuCategory,MenuItem
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
    restaurant = get_object_or_404(Restaurant, restaurant_slug=restaurant_slug)
    restaurant_imgs = restaurant.restaurant_imgs.all()
    menu_categories = restaurant.menu_categories.all()
    social_icons = restaurant.social_icons.all()

    return render(request,"food/restaurant-details.html",{
        "restaurant_imgs": restaurant_imgs,
        "social_icons":social_icons,
        "restaurant":restaurant,
        "menu_categories":menu_categories
    })




# list of all restaurants
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request,"food/restaurants_list.html",{
        "restaurants":restaurants
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

    