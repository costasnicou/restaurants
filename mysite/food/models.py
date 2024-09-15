from django.db import models
from django.utils.text import slugify
# Create your models here.

# one restaurant has many categories
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_image = models.ImageField(default='restaurant_default.jpg',upload_to='restaurant_images')
    restaurant_location = models.CharField(max_length=100)
    restaurant_slug = models.SlugField(unique=True,blank=True)  # Add this field for slug-based lookups
    restaurant_phone = models.IntegerField(unique=True)
    restaurant_about= models.TextField()
    restaurant_featured = models.BooleanField(blank=True)

    
    def save(self, *args, **kwargs):
        if not self.restaurant_slug:
            self.restaurant_slug = slugify(self.restaurant_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.restaurant_name
    
class RestaurantImg(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="restaurant_imgs")
    name = models.CharField(max_length=100)
    restaurant_image = models.ImageField(default='restaurant_details-img.jpg',upload_to='restaurant_details_images')

    def __str__(self):
        return f"{self.name}: {self.restaurant}"

class MenuCategory(models.Model):
    restaurant= models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="menu_categories")
    menu_name = models.CharField(max_length=100)
    menu_slug = models.SlugField(blank=True)  # Add this 
    menu_image = models.ImageField(default='menu_category_default.jpg',upload_to='restaurant_images')

    def save(self, *args, **kwargs):
        if not self.menu_slug:
            self.menu_slug = slugify(self.menu_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}: {self.menu_name}: {self.restaurant}"


class MenuItem(models.Model):
    menu_category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name="menu_items")
    menu_item_name = models.CharField(max_length=100)
    menu_item_image = models.ImageField(default='menu_item_default.jpg',upload_to='menu_item_images')
    menu_item_price = models.IntegerField()


    def __str__(self):
        return f"{self.id}: {self.menu_item_name}"
    

class SocialMedia(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="social_icons")
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    social_image = models.ImageField(default='social_icon.jpg',upload_to='social_icon_images')

    def __str__(self):
        return f"{self.name}: {self.restaurant}"
