# Generated by Django 3.0.6 on 2020-06-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200603_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(default='base.jpg', upload_to='images/'),
        ),
    ]
