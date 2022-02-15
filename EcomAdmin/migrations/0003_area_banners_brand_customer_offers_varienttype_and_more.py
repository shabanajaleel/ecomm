# Generated by Django 4.0.2 on 2022-02-14 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0002_delete_area_delete_banners_delete_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=30)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Area',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=100)),
                ('banner_url', models.URLField(max_length=100)),
                ('banner_image', models.FileField(upload_to='images/Banner')),
                ('app_banner_image', models.FileField(upload_to='images/Banner_app')),
                ('is_intermediate', models.BooleanField(default=True)),
                ('display_order', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Banner',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_image', models.ImageField(upload_to='images/brand')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Brand',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=20)),
                ('conf_password', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Customer',
                'ordering': ['-registered_date'],
            },
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=100)),
                ('offer_image', models.ImageField(upload_to='images/offers')),
                ('offer_app_image', models.ImageField(upload_to='images/offers/app_image')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=30)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Offers',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='VarientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient_name', models.CharField(max_length=100)),
                ('display_order', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Varient Type',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='VarientValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient_values', models.CharField(max_length=100)),
                ('display_order', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('varient_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.varienttype')),
            ],
            options={
                'db_table': 'Varient Values',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=10)),
                ('postoffice', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=30)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.area')),
            ],
            options={
                'db_table': 'Pincode',
                'ordering': ['-Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Catogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogory_name', models.CharField(max_length=100)),
                ('catogory_image', models.ImageField(upload_to='images/catogory')),
                ('display_order', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.catogory')),
            ],
            options={
                'db_table': 'Catogory',
                'ordering': ['-Created_at'],
            },
        ),
    ]
