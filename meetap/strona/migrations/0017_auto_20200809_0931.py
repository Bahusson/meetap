# Generated by Django 3.0.3 on 2020-08-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0016_auto_20200805_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilenames',
            name='showme_sexevents',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='showme_sexevents_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='showme_sexevents_pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
