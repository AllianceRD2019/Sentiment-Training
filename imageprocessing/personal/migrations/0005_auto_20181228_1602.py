# Generated by Django 2.1.4 on 2018-12-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20181228_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='documents'),
        ),
    ]
