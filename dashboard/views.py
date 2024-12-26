from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from .models import Category, Expense, Income
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def download_report(request):
    expneses = list(Expense.objects.filter(author=request.user).values())
    file_name = f"{request.user}_expenses.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(str(expneses))
    with open(file_name, encoding="utf-8") as f:
        data = f.read()
    response = HttpResponse(data, content_type="text/plain")
    if response.status_code == 200:
        response["Content-Disposition"] = f'attachment; filename="{file_name}"'
        return response


def add_transactions(request):
    return render(request, "dashboard/add_transactions.html")


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "dashboard/index.html"

    def get_queryset(self):
        return Category.objects.filter(author=self.request.user)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "dashboard/detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        incomes = Income.objects.filter(category_id=self.object.id)
        expenses = Expense.objects.filter(category_id=self.object.id)
        context["incomes"] = incomes
        context["expenses"] = expenses
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "dashboard/add_category.html"
    fields = ("title",)
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "dashboard/confirm_delete.html"
    fields = ("title",)
    success_url = reverse_lazy("category_list")


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "dashboard/confirm_delete.html"
    fields = ("title", "category", "total")
    success_url = reverse_lazy("category_list")


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = "dashboard/confirm_delete.html"
    fields = ("title", "category", "total")
    success_url = reverse_lazy("category_list")


class IncomeCreateView(CreateView):
    model = Income
    fields = ("title", "category", "total")
    template_name = "dashboard/add_income.html"
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ("title", "category", "total")
    template_name = "dashboard/add_expense.html"
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
