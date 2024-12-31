from django.contrib import admin

from .models import Category, Expense, Income


class InlineExpenseModel(admin.TabularInline):
    model = Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (InlineExpenseModel,)


admin.site.register(Income)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author")
