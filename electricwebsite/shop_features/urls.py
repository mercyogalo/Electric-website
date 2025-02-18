from django.urls import path
from . import views



app_name="shop_features"

urlpatterns = [
    path("", views.home,name="home"),
    path("product/<int:pk>", views.product, name="product"),
    path("store/", views.store, name="store"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
     path("register/", views.register_user, name="register"),
     path("contact/", views.contact,name="contact"),
     path("profile/", views.profile,name="profile"),
     path("order/", views.order,name="order"),
]
