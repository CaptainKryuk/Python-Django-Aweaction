# Generated by Django 2.0.3 on 2018-04-06 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20180406_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique_for_date='publish'),
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
