from django.urls import path

from .views import index, add_category, add_transactions

urlpatterns = [
    path("", index, name="index"),
    path("/add_category", add_category, name="add_category"),
    path("/add_transactions", add_transactions, name="add_transactions"),
]
