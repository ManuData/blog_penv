# Generated by Django 4.0.6 on 2023-04-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_image_article_manualpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_category',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
