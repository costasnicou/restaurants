from django.contrib import admin
from .models import Restaurant,MenuCategory,MenuItem,SocialMedia,RestaurantImg
# Register your models here.


admin.site.register(SocialMedia)
admin.site.register(RestaurantImg)
# admin.site.register(MenuCategory)
# admin.site.register(MenuItem)
# Inline for MenuCategory in RestaurantAdmin
class MenuCategoryInline(admin.TabularInline):
    model = MenuCategory
    extra = 1
    fields = ['menu_name', 'menu_image']
    readonly_fields = ['menu_name']  # Make the menu name read-only
    show_change_link = True  # Enable linking to the MenuCategory's detail page

# Register Restaurant with inlines
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'restaurant_location', 'restaurant_phone']
    inlines = [MenuCategoryInline]  # Show MenuCategories within Restaurant admin

# Custom admin for MenuCategory to filter by current Restaurant
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','menu_name', 'restaurant']
    list_filter = ['restaurant']  # Allows filtering by restaurant in the MenuCategory list view

    def get_queryset(self, request):
        """
        Limit the queryset to only show MenuCategories for the current Restaurant if present in the request.
        """
        qs = super().get_queryset(request)
        # If there's a specific Restaurant being accessed, filter MenuCategories by it
        restaurant_id = request.GET.get('restaurant')
        if restaurant_id:
            qs = qs.filter(restaurant__id=restaurant_id)
        return qs
    
# Custom filter to filter MenuItem by Restaurant
class RestaurantFilter(admin.SimpleListFilter):
    title = 'restaurant'  # Display title in the filter sidebar
    parameter_name = 'restaurant'  # The URL parameter used in the filter

    def lookups(self, request, model_admin):
        # Provide a list of options to filter by (list of restaurants)
        restaurants = Restaurant.objects.all()
        return [(restaurant.id, restaurant.restaurant_name) for restaurant in restaurants]

    def queryset(self, request, queryset):
        # Filter the MenuItem queryset based on the selected restaurant
        if self.value():
            return queryset.filter(menu_category__restaurant__id=self.value())
        return queryset

# Register MenuItemAdmin with the custom filter
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['menu_item_name', 'menu_item_price', 'menu_category']  # Display fields
    list_filter = [RestaurantFilter]  # Add custom filter for restaurants