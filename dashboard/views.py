from django.shortcuts import render

from .models import Category


def index(request):
    categories = Category.objects.filter(author=request.user)
    context = {"categories": categories}
    return render(request, "dashboard/index.html", context=context)


def add_category(request):
    return render(request, "dashboard/add_categories.html")


def add_transactions(request):
    return render(request, "dashboard/add_transactions.html")
