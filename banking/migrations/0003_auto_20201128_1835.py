# Generated by Django 3.1.3 on 2020-11-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
