# Generated by Django 4.1.5 on 2023-02-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='animales'),
        ),
    ]
