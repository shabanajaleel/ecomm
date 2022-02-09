# Generated by Django 4.0.2 on 2022-02-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannner_name', models.CharField(max_length=100)),
                ('banner_url', models.CharField(max_length=100)),
                ('banner_image', models.FileField(upload_to='images/Banner')),
                ('app_banner_image', models.FileField(upload_to='images/Banner_app')),
                ('display_order', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Banner',
            },
        ),
    ]
