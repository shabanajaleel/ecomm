# Generated by Django 4.0.2 on 2022-02-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0012_alter_pincode_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='brand_image',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='status',
        ),
    ]
