# Generated by Django 4.0.2 on 2022-03-09 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0018_alter_address_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.customer'),
        ),
    ]