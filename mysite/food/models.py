from django.db import models

# Create your models here.

# one restaurant has many categories
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_image = models.CharField(max_length=1000,default="https://900degreespizza.com/wp-content/uploads/2019/10/chairs-cutlery-fork-9315.jpg")
    restaurant_location = models.CharField(max_length=100)
    def __str__(self):
        return self.restaurant_name
    


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=1000,default="https://st3.depositphotos.com/4060975/18243/v/450/depositphotos_182439216-stock-illustration-flat-icon-food-menu.jpg")
    restauraunt_belongs=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="categories_by_restaurant")

    def __str__(self):
        return self.category_name



# food menu item
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE,related_name="foods_by_category")
    # belongs = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="foods")
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()

    # adding image links
    item_image = models.CharField(max_length=1000,default="https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg")

    def __str__(self):
        return f"{self.item_name}"