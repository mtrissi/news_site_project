# Generated by Django 2.2.11 on 2020-03-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
