# Generated by Django 4.0.2 on 2022-02-10 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0016_alter_brand_options_brand_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catogory',
            options={'ordering': ['-Created_at']},
        ),
        migrations.AddField(
            model_name='catogory',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 10, 5, 34, 39, 817452, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
