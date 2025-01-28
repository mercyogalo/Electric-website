from django.urls import path
from . import views



app_name="shop_features"

urlpatterns = [
    path("", views.home,name="home"),
    path("checkout/", views.checkout, name="checkout"),
    path("product/", views.product, name="product"),
    path("store/", views.store, name="store"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
     path("register/", views.register_user, name="register"),
]
