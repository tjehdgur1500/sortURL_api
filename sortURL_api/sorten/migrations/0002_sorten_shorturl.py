# Generated by Django 3.0.7 on 2020-06-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorten', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorten',
            name='shorturl',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]