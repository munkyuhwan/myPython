# Generated by Django 2.2.6 on 2019-10-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_complete_cnt', models.IntegerField()),
                ('over_order_cnt', models.IntegerField()),
                ('pickup_avg', models.IntegerField()),
                ('pickup_complete_avg', models.IntegerField()),
                ('order_avg_distance', models.IntegerField()),
                ('order_acc_distance', models.IntegerField()),
                ('pickup_request_complete', models.IntegerField()),
                ('pickup_20min', models.IntegerField()),
                ('pickup_40min', models.IntegerField()),
            ],
        ),
    ]
