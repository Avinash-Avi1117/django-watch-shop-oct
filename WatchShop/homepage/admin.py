from django.contrib import admin
from .models import Watches
from .models import WatchesUploads
from .models import wichlist
from .models import cartlist
from .models import WatchReview
from .models import CartItem
# Register your models here.

admin.site.register(Watches)
admin.site.register(wichlist)
admin.site.register(cartlist)


class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','descripation','image','count')
    list_filter = ('name','price')
    search_fields = ['name', 'descripation']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)
admin.site.register(CartItem)

class WatchReviewAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'product', 'review_text', 'rating')
    list_filter = ('rating', 'product')
admin.site.register(WatchReview, WatchReviewAdmin)