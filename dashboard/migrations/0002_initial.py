# Generated by Django 5.1.4 on 2024-12-31 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Category author'),
        ),
        migrations.AddField(
            model_name='expense',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Expenses author'),
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='dashboard.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='income',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Income author'),
        ),
        migrations.AddField(
            model_name='income',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income', to='dashboard.category', verbose_name='Category'),
        ),
    ]
