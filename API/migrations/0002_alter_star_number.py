# Generated by Django 5.0.1 on 2024-02-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
