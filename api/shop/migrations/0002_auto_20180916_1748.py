# Generated by Django 2.1.1 on 2018-09-16 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tax_amount',
        ),
    ]