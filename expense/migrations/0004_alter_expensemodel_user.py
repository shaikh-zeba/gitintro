# Generated by Django 4.2.6 on 2023-10-12 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0003_expensemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense', to=settings.AUTH_USER_MODEL),
        ),
    ]