# Generated by Django 2.0.2 on 2018-04-03 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercicio', '0004_auto_20180403_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercicio',
            name='codigo_desenvolvido',
        ),
    ]
