from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Watches, WatchesUploads, wichlist, cartlist, WatchReview, CartItem
from .forms import uploadform
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t' : watches}
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def Upload(request):
    if request.method == 'POST':
        form = uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = uploadform()

    return render(request, 'WatchUpload.html', {'form': form} )

#LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login


def login_user(requset):
    if requset.method == 'POST':
        form = AuthenticationForm(requset, data=requset.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = user_name, password = password)

            if user is not None :
                login(requset, user)
                return redirect('home')
            else:
                return render(requset,'login.html', {'form': form})
            
    else:
        form = AuthenticationForm()
    return render(requset, 'login.html', {'form': form} )

#signup
def signup_user(requset):
    if requset.method == 'POST':
        form = UserCreationForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(requset,'signup.html', {'form': form})



#LOGOUT
def logout_user(requset):
    logout(requset)
    return redirect('home')

from django.shortcuts import get_object_or_404
def show_product(requset, id):
    product = get_object_or_404(WatchesUploads, id=id)
    review = WatchReview.objects.filter(product=product)
    return render(requset, "product.html", {"product": product, "reviews": review} )

def addtowish(request, id):
    user = request.user
    product = WatchesUploads.objects.get(id=id)
    obj1, created = wichlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

@login_required(login_url='login')
def show_wishlist(request):
    user = request.user
    wish_object = wichlist.objects.get(user=user)
    return render(request, "wishlist.html", {"user_products": wish_object.products.all()})

def removewish(request, id):
    product_rm = WatchesUploads.objects.get(id=id)
    wish_obj = wichlist.objects.get(user=request.user)
    wish_obj.products.remove(product_rm)
    return render(request, 'wishlist.html', {"user_products": wish_obj.products.all()})

def addtocart(request, id):
    # user = request.user
    # product = WatchesUploads.objects.get(id=id)
    # obj1, created = cartlist.objects.get_or_create(user=user)
    # obj1.products.add(product)
    # obj1.save()
    # return redirect('home')
    user_cart, created = cartlist.objects.get_or_create(user = request.user)

    product = WatchesUploads.objects.get(id=id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=user_cart)
    cart_item.product=product
    cart_item.save()

    return redirect('home')

@login_required(login_url='login')
def show_cartlist(request):
    #  user = request.user
    #  cart_object = cartlist.objects.get(user=user)
    #  return render(request, "cart.html", {"user_products": cart_object.products.all()})
    user_cart, created = cartlist.objects.get_or_create(user = request.user)

    cart_object = user_cart.cartitem_set.all()
    return render(request, "cart.html", {"user_products": cart_object})

def removeCart(request, id):
    product_rm = WatchesUploads.objects.get(id=id)
    cart_obj = cartlist.objects.get(user=request.user)
    cart_obj.products.remove(product_rm)
    return render(request, "cart.html", {"user_products": cart_obj.products.all()})