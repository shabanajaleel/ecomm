# Generated by Django 4.0.2 on 2022-02-21 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0004_alter_productimage_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='product_varients',
            options={'ordering': ['-created_at']},
        ),
    ]