# Generated by Django 3.2.3 on 2021-05-31 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(verbose_name='data publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Relacionada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(max_length=200)),
                ('materia_relacionada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.materia')),
            ],
        ),
    ]
