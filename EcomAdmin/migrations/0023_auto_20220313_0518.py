# Generated by Django 3.2.10 on 2022-03-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0022_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='conf_password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]