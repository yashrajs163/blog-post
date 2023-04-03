# Generated by Django 4.1.7 on 2023-03-23 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blobing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]