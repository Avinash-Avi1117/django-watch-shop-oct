from django.contrib import admin
from django.urls import path
from .views import Home, About, Upload, login_user, logout_user, signup_user, show_product, addtowish, show_wishlist, removewish, addtocart, show_cartlist, removeCart
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('' , Home , name="home"),
    path('about' , About , name="about"),
    path('upload' , Upload, name="upload"),
    path( 'login', login_user, name='login'),
    path( 'signup', signup_user, name='signup'),
    path( 'logout', logout_user, name='logout'),
    path( 'product/<int:id>', show_product, name='product'),
    path( 'addtowish/<int:id>', addtowish, name='addtowish'),
    path( 'wishlist', show_wishlist, name="show_wishlist"),
    path( 'removewish/<int:id>', removewish, name='removewish'),
    path( 'addtocart/<int:id>', addtocart, name='addtocart'),
    path( 'cartlist', show_cartlist, name="show_cartlist"),
    path( 'removecart/<int:id>', removeCart, name='removecart')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)