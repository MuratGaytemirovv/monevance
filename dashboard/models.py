from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField("Title", max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Category author"
    )


class Expense(models.Model):
    title = models.CharField("Title", max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Expenses author"
    )
    total = models.PositiveIntegerField("Total expenses")


class Income(models.Model):
    title = models.CharField("Title", max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Income author"
    )
    total = models.PositiveIntegerField("Total income")
