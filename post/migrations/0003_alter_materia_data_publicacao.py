# Generated by Django 3.2.3 on 2021-06-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_materia_img_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='data_publicacao',
            field=models.DateField(verbose_name='data publicacao'),
        ),
    ]
