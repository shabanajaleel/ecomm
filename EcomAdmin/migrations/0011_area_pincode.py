# Generated by Django 4.0.2 on 2022-02-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0010_offers_alter_varienttype_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=30)),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=10)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.area')),
            ],
            options={
                'db_table': 'Pincode',
            },
        ),
    ]
