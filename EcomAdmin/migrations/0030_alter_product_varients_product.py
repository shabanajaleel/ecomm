# Generated by Django 4.0.2 on 2022-03-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0029_alter_product_varients_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_varients',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.product'),
        ),
    ]
