from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField("Title", max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Category author"
    )

    def __str__(self):
        return self.title


class Expense(models.Model):
    # TODO: add created_at_field
    title = models.CharField("Title", max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Category",
        related_name="expenses",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Expenses author"
    )
    total = models.PositiveIntegerField("Total expenses")

    def __str__(self):
        return self.title


class Income(models.Model):
    title = models.CharField("Title", max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Category",
        related_name="income",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Income author"
    )
    total = models.PositiveIntegerField("Total income")

    def __str__(self):
        return self.title
