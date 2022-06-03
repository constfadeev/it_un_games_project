# Generated by Django 4.0.4 on 2022-05-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('city', models.CharField(max_length=250, verbose_name='Город')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('tags', models.CharField(verbose_name='Теги')),
            ],
        ),
    ]
