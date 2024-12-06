from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Watches(models.Model):
    name = models.CharField(max_length=100)
    descripation = models.TextField()
    price= models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class WatchesUploads(models.Model):
    name = models.CharField(max_length=100)
    descripation = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='watches_images/')
    count = models.IntegerField(default= 1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class wichlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class cartlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    user = models.ForeignKey(cartlist, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=1)

class WatchReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(WatchesUploads,on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveBigIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)