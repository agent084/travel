from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from boilerplate.forms import ReviewForm, SignupForm, SigninForm
from boilerplate.models import Product, Category
from boilerplate.serializer import ProductSerializer


def index(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    context = {"products": products, "categories": categories}
    return render(request, "boilerplate/index.html", context)


def about(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    context = {"products": products, "categories": categories}
    return render(request, "boilerplate/about-us.html", context)


def packages(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    context = {"products": products, "categories": categories}
    return render(request, "boilerplate/packages.html", context)


def contact(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    context = {"products": products, "categories": categories}
    return render(request, "boilerplate/contact.html", context)


def categories(request, slug):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(active=True, category=cat)
    categories = Category.objects.filter(active=True)
    context = {
        "products": products,
        "categories": categories,
        "title": cat.name + " - Categories",
    }
    return render(request, "boilerplate/store.html", context)


def packages_single(request, slug):
    product = Product.objects.get(active=True, slug=slug)
    categories = Category.objects.filter(active=True)
    context = {"product": product, "categories": categories}
    return render(request, "boilerplate/packages_single.html", context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User saved")
            return redirect("boilerplate:signin")
        else:
            messages.error(request, "Error in form")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "boilerplate/signup.html", context)


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        # username = req.POST["username"]
        # password = req.POST["password"]
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("boilerplate:index")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    context = {"form": form}
    return render(request, "boilerplate/signin.html", context)


def signout(request):
    logout(request)
    return redirect("boilerplate:signin")


def book_trip(request):
    return render(request, "boilerplate/book-trip.html", context=None)

