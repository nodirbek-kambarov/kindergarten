# Generated by Django 3.1.7 on 2021-04-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_photo',
            field=models.ImageField(default='-', upload_to='workersimg'),
        ),
    ]
