# Generated by Django 4.0.4 on 2022-05-08 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=255)),
                ('short_code', models.CharField(blank=True, max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_visited', models.DateTimeField(blank=True, null=True)),
                ('visit_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]