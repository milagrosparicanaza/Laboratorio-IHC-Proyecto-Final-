# Generated by Django 2.1.5 on 2020-08-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='comida',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]