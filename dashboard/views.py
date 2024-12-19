from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Category, Expense
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy


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


class CategoryListView(ListView):
    model = Category
    template_name = "dashboard/index.html"

    def get_queryset(self):
        return Category.objects.filter(author=self.request.user)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "dashboard/detail.html"


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
    template_name = "dashboard/confirm_delete_category.html"
    fields = ("title",)
    success_url = reverse_lazy("category_list")
