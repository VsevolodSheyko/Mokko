# Generated by Django 4.2 on 2023-04-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeehouse', '0002_alter_freetable_coffeeshop_alter_order_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='date_joined',
            field=models.DateField(null=True),
        ),
    ]
