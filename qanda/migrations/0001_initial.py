# Generated by Django 3.0.5 on 2020-12-24 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='question')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='qanda.Question')),
            ],
        ),
    ]
