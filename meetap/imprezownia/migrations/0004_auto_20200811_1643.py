# Generated by Django 2.2.4 on 2020-08-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imprezownia', '0003_eventsmenunames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsmenunames',
            old_name='my_teplates',
            new_name='my_templates',
        ),
        migrations.RenameField(
            model_name='eventsmenunames',
            old_name='my_teplates_en',
            new_name='my_templates_en',
        ),
        migrations.RenameField(
            model_name='eventsmenunames',
            old_name='my_teplates_pl',
            new_name='my_templates_pl',
        ),
    ]
