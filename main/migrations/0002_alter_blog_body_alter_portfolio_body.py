# Generated by Django 4.0.4 on 2022-05-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
