# Generated by Django 4.0.5 on 2022-07-04 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_aboutuspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutuspage',
            name='about1',
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='about2',
        ),
    ]