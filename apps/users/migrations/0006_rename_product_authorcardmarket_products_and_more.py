# Generated by Django 5.0.1 on 2024-02-29 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_authorlike_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorcardmarket',
            old_name='product',
            new_name='products',
        ),
        migrations.AddField(
            model_name='authorcardmarket',
            name='authorS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]