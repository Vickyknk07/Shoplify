# Generated by Django 4.0 on 2021-12-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
