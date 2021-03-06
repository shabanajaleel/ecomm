# Generated by Django 4.0.2 on 2022-02-19 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0002_delete_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Thumbnail_image', models.ImageField(null=True, upload_to='Products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.product')),
            ],
            options={
                'db_table': 'Product_image',
            },
        ),
    ]
