# Generated by Django 5.0.3 on 2024-03-25 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='img',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>'),
        ),
        migrations.AlterField(
            model_name='esper',
            name='img',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>'),
        ),
    ]
