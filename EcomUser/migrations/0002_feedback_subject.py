# Generated by Django 4.0.2 on 2022-02-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
