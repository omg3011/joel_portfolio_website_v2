# Generated by Django 3.1.3 on 2020-12-12 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='noOfProjects',
        ),
    ]
