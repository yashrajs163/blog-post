# Generated by Django 4.1.7 on 2023-03-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blobing', '0003_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
