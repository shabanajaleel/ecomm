# Generated by Django 4.0.2 on 2022-03-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0016_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='landmark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
