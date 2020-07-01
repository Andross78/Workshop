# Generated by Django 2.2.6 on 2020-06-21 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0006_car_insurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('process', models.ManyToManyField(related_name='ordered_carts', to='pancar.Process')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]