# Generated by Django 4.0.2 on 2022-02-27 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0011_remove_coupencode_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupencode',
            options={'ordering': ['-id']},
        ),
    ]
