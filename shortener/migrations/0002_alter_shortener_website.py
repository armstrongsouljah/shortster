# Generated by Django 4.0.4 on 2022-05-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='website',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
