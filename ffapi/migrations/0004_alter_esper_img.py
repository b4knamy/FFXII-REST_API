# Generated by Django 5.0.3 on 2024-03-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffapi', '0003_alter_character_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esper',
            name='img',
            field=models.ImageField(blank=True, upload_to='esper'),
        ),
    ]
