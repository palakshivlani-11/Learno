# Generated by Django 2.1.6 on 2019-02-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_question_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer'),
        ),
    ]
