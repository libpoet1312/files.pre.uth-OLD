# Generated by Django 2.2.7 on 2019-12-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_auto_20191219_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='course',
            field=models.ManyToManyField(help_text='Select a course for this file', to='www.Course'),
        ),
    ]
