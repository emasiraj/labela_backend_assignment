# Generated by Django 4.0.3 on 2022-03-14 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autocompany', '0007_rename_shoppingcart_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered_date',
            new_name='delivery_datetime',
        ),
    ]
