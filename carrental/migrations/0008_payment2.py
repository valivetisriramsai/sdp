# Generated by Django 3.2.2 on 2021-05-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0007_rename_status_book_status1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholdername', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('cardnumber', models.BigIntegerField()),
            ],
        ),
    ]
