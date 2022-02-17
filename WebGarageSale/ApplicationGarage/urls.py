from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("magbenta/", views.magbenta, name="magbenta"),
    path("BagongBenta", views.BagongBenta, name="bagongbenta"),
    path("KuhainAngListing", views.getListings, name="KuhainAngListing")
]
