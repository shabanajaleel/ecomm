
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAdmin', '0016_alter_customer_phone'),
        ('EcomUser', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_quantity', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomAdmin.customer')),
            ],
        ),
    ]
