# Generated by Django 3.2.13 on 2023-08-14 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog.author'),
        ),
    ]