# Generated by Django 3.1 on 2020-08-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0010_auto_20200817_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedcart',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
