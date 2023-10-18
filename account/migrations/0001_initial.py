# Generated by Django 3.0.14 on 2023-09-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]
