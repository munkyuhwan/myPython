# Generated by Django 2.2.6 on 2019-10-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_cnt', models.IntegerField(max_length=11)),
                ('commision_amt', models.IntegerField(max_length=11)),
                ('after_commission', models.IntegerField(max_length=11)),
                ('jingsu', models.IntegerField(max_length=11)),
            ],
        ),
    ]
