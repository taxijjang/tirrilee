# Generated by Django 3.0.6 on 2020-06-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20200604_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]