# Generated by Django 2.2.6 on 2020-01-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='f_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='title',
            name='mail',
            field=models.EmailField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='title',
            name='phone',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
