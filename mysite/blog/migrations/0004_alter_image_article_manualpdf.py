# Generated by Django 4.0.6 on 2023-03-05 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articles_image_article_list_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.articles'),
        ),
        migrations.CreateModel(
            name='ManualPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdf')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='blog.articles')),
            ],
        ),
    ]