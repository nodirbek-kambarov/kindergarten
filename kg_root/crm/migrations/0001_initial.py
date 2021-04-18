# Generated by Django 3.1.7 on 2021-04-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=200)),
                ('order_phone', models.IntegerField(max_length=26)),
                ('order_text', models.TextField(default=None)),
                ('order_dt', models.DateField(auto_now=True)),
            ],
        ),
    ]