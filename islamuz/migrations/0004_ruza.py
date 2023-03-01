# Generated by Django 4.1.7 on 2023-03-01 13:53

import ckeditor.fields
from django.db import migrations, models
import hitcount.models


class Migration(migrations.Migration):

    dependencies = [
        ('islamuz', '0003_namoz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('body', ckeditor.fields.RichTextField()),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
