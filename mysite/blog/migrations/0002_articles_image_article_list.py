# Generated by Django 4.0.6 on 2022-12-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image_article_list',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
