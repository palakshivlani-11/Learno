# Generated by Django 2.1.6 on 2019-02-13 22:16

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190213_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorful.fields.RGBColorField(default='#007bff'),
        ),
    ]
