# Generated by Django 2.0.5 on 2018-05-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180527_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='contest',
            field=models.ImageField(upload_to='news/%Y/%m/%d'),
        ),
    ]
