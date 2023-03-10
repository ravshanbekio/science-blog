# Generated by Django 4.1.6 on 2023-03-04 16:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle_en',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle_ru',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle_uz',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_uz',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
