from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>/", views.category, name="category"),
    path("magbenta/", views.magbenta, name="magbenta"),
    path("BagongBenta/", views.BagongBenta, name="bagongbenta"),
    path("KuhainAngListing/<str:categ>", views.getListings, name="KuhainAngListing")
]
