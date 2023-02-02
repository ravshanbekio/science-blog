# Generated by Django 4.1.6 on 2023-02-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(related_name='blogs', to='blog.category'),
        ),
    ]
