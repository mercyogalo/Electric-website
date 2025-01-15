from django.urls import path
from . import views



app_name="shop_features"

urlpatterns = [
    path("", views.home,name="home"),
]
