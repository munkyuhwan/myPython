# Generated by Django 2.2.6 on 2019-10-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_list', '0002_remove_orderlist_address_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='address_from',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]