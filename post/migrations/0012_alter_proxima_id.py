# Generated by Django 3.2.3 on 2021-06-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20210607_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxima',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
