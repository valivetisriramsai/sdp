# Generated by Django 3.2.2 on 2021-05-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]