# Generated by Django 2.0.2 on 2018-04-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercicio', '0005_remove_exercicio_codigo_desenvolvido'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='codigo',
            field=models.CharField(default='0', max_length=1000),
            preserve_default=False,
        ),
    ]
