# Generated by Django 5.0.3 on 2024-03-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffapi', '0004_alter_esper_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.CharField(max_length=6),
        ),
    ]