# Generated by Django 3.2.2 on 2021-05-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0004_rename_payement_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
