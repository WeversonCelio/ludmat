# Generated by Django 3.2.3 on 2021-06-09 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_proxima_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxima',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
