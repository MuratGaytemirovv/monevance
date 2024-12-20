from django.urls import path

from .views import (
    add_transactions,
    download_report,
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
    path("", CategoryListView.as_view(), name="category_list"),
    path("add_category/", CategoryCreateView.as_view(), name="add_category"),
    path("add_transactions/", add_transactions, name="add_transactions"),
    path("download_report", download_report, name="download_report"),
    path("add_income/", IncomeCreateView.as_view(), name="add_income"),
    path("add_expense/", ExpenseCreateView.as_view(), name="add_expense"),
    path("<pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("<pk>/delete", CategoryDeleteView.as_view(), name="category_delete_view"),
    path("<pk>/delete_income", IncomeDeleteView.as_view(), name="income_delete_view"),
    path(
        "<pk>/delete_expense", ExpenseDeleteView.as_view(), name="expense_delete_view"
    ),
]
