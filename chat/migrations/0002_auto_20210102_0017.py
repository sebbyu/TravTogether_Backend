# Generated by Django 3.0.5 on 2021-01-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='title'),
        ),
    ]
