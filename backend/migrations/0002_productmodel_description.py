# Generated by Django 2.1.5 on 2019-01-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=models.TextField(default='description', max_length=2000),
            preserve_default=False,
        ),
    ]
