# Generated by Django 2.0.1 on 2018-01-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0003_coin_pair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='btc_price',
            field=models.DecimalField(decimal_places=8, max_digits=15),
        ),
        migrations.AlterField(
            model_name='coin',
            name='price',
            field=models.DecimalField(decimal_places=8, max_digits=15),
        ),
    ]