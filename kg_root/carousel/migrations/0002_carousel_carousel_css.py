# Generated by Django 3.1.7 on 2021-04-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='carousel_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS'),
        ),
    ]