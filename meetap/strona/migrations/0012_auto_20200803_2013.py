# Generated by Django 3.0.3 on 2020-08-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0011_auto_20200803_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='regnames',
            name='send_me',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regnames',
            name='send_me_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='send_me_pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]