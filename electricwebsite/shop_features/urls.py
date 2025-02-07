from django.urls import path
from . import views



app_name="shop_features"

urlpatterns = [
    path("", views.home,name="home"),
    path("shipping/", views.shipping, name="shipping"),
    path("product/<int:pk>", views.product, name="product"),
    path("store/", views.store, name="store"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
     path("register/", views.register_user, name="register"),
     path("cart_summary/", views.cart_summary,name="cart_summary"),
     path("cart_add/", views.cart_add,name="cart_add"),
     path("cart_update/", views.cart_update,name="cart_update"),
     path("cart_delete/", views.cart_delete,name="cart_delete"),
     path("contact/", views.contact,name="contact"),
     path("order/", views.order,name="order"),
]
