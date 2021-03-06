# Generated by Django 3.0.6 on 2020-06-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='introduce',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, default='media/base.jpg', upload_to='media/'),
        ),
    ]
