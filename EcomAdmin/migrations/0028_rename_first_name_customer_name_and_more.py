# Generated by Django 4.0.2 on 2022-03-18 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0027_alter_customer_session_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
