# Generated by Django 3.2.4 on 2021-06-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
