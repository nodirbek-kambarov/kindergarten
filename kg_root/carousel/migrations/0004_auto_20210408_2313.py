# Generated by Django 3.1.7 on 2021-04-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0003_auto_20210406_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='carousel_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS'),
        ),
    ]
