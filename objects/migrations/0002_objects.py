# Generated by Django 4.0 on 2022-02-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little_desc', models.CharField(max_length=300, verbose_name='Краткое описание')),
                ('full_desc', models.TextField(verbose_name='Полное описание')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('pic', models.ImageField(upload_to='media', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]
