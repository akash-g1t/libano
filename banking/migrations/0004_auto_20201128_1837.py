# Generated by Django 3.1.3 on 2020-11-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_auto_20201128_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='url',
            field=models.CharField(max_length=100, verbose_name='Address'),
        ),
    ]
