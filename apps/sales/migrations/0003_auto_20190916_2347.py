# Generated by Django 2.2.5 on 2019-09-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20190611_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='stripe_coupon_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
