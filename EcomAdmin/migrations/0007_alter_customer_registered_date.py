# Generated by Django 4.0.2 on 2022-02-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0006_alter_product_status_alter_product_varients_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='registered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
