# Generated by Django 3.0.6 on 2020-06-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cellphone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='users',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]
