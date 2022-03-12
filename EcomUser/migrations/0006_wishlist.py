# Generated by Django 4.0.2 on 2022-03-07 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0016_alter_customer_phone'),
        ('EcomUser', '0005_cart_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.product_varients')),
            ],
        ),
    ]