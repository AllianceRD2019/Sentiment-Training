# Generated by Django 2.1.5 on 2019-02-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_auto_20190204_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='score',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
