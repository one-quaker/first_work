# Generated by Django 2.2 on 2019-06-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190615_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Работа'), (1, 'Волонтерство'), (2, 'Стажировка')], default=0),
        ),
    ]
