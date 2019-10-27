from django.urls import path

from . import views

app_name = "boilerplate"

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("about-us.html", views.about, name="about"),
    path("packages.html", views.packages, name="packages"),
    path("contact.html", views.contact, name="contact"),
    path("shop-single/<slug>/", views.shop_single, name="shop_single"),
    path("book-trip.html", views.book_trip, name="book_trip"),
    path("categories/<slug>/", views.categories, name="categories"),
    path("join-us.html", views.join, name="join-us"),
]
