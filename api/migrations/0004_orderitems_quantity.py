# Generated by Django 3.0.6 on 2020-08-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200828_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
