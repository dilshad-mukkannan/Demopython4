# Generated by Django 3.1.7 on 2023-05-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
