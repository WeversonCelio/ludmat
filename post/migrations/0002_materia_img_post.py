# Generated by Django 3.2.3 on 2021-06-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='img_post',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]
