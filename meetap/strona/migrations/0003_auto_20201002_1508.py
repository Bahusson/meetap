# Generated by Django 3.1 on 2020-10-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_auto_20201001_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageskin',
            name='dividerimagedefault',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
        migrations.AddField(
            model_name='pageskin',
            name='taxpanelimagedefault',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
    ]
