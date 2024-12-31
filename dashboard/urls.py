from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    download_report,
    home,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryDeleteView,
    IncomeCreateView,
    ExpenseCreateView,
    IncomeDeleteView,
    ExpenseDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path(
        "category_list",
        cache_page(60)(CategoryListView.as_view()),
        name="category_list",
    ),
    path("add_category/", CategoryCreateView.as_view(), name="add_category"),
    path("download_report", download_report, name="download_report"),
    path("add_income/", IncomeCreateView.as_view(), name="add_income"),
    path("add_expense/", ExpenseCreateView.as_view(), name="add_expense"),
    path("<int:pk>", CategoryDetailView.as_view(), name="category_detail"),
    path("<int:pk>/delete", CategoryDeleteView.as_view(), name="category_delete_view"),
    path(
        "<int:pk>/delete_income", IncomeDeleteView.as_view(), name="income_delete_view"
    ),
    path(
        "<int:pk>/delete_expense",
        ExpenseDeleteView.as_view(),
        name="expense_delete_view",
    ),
]
