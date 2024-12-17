from django.urls import path

from .views import index, add_category, add_transactions

urlpatterns = [
    path("", index, name="index"),
    path("add_categories", add_category, name="add_categories"),
    path("add_transactions", add_transactions, name="add_transactions"),
]
