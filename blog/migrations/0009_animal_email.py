# Generated by Django 4.1.5 on 2023-01-28 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]