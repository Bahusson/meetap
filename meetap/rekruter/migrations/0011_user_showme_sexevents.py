# Generated by Django 3.0.3 on 2020-08-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0010_auto_20200804_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='showme_sexevents',
            field=models.BooleanField(default=False, verbose_name='showme_sexevents'),
        ),
    ]
