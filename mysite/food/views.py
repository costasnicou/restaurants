from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,Restaurant,ItemCategory
# Create your views here.


# index route on url localhost
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request,"food/index.html",{
        "restaurants":restaurants
    })


# restaurant_details
def restaurant_details(request,restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menu_categories = restaurant.categories_by_restaurant.all()
    return render(request,"food/restaurant-details.html",{
        "restaurant":restaurant,
        "menu_categories":menu_categories
    })


def menu_details(request,category_id):
    
    item_category = ItemCategory.objects.get(pk=category_id)
    menu_items = item_category.foods_by_category.all()

    # menuitems = restaurant.foods.all()
    return render(request,"food/menu_details.html",{
        "item_category":item_category,
        "menu_items":menu_items,
    })
