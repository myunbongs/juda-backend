# Generated by Django 4.0.6 on 2022-07-17 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_category_tag_post_create_dt_post_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
