# Generated by Django 2.0.3 on 2018-04-06 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-title',)},
        ),
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]
