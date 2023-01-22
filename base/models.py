from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.


LABEL_CHOICES = (
    ('p','primary'),
    ('s','secondary'),
    ('d','danger')
)

class Category(models.Model):
    cat = models.CharField(max_length=100)

    def __str__(self):
        return self.cat
    


    

class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    label = models.CharField(choices=LABEL_CHOICES,max_length=1)
    slug = models.SlugField(default=True)
    description = models.TextField(default=True)
    



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('base:product',kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('base:add-to-cart',kwargs={
            'slug':self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('base:remove-from-cart',kwargs={
            'slug':self.slug
        })


    

   
        

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'


    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    startDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField()

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total 