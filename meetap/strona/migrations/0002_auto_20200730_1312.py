# Generated by Django 3.0.3 on 2020-07-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blognames',
            options={'verbose_name_plural': 'BlogNames'},
        ),
        migrations.AlterModelOptions(
            name='pagenames',
            options={'verbose_name_plural': 'PageNames'},
        ),
        migrations.AlterModelOptions(
            name='regnames',
            options={'verbose_name_plural': 'RegNames'},
        ),
        migrations.RenameField(
            model_name='pageskin',
            old_name='eskslogo_main',
            new_name='avatarimagedefault',
        ),
        migrations.RenameField(
            model_name='pageskin',
            old_name='fileimagedefault',
            new_name='meetaplogo_main',
        ),
        migrations.RemoveField(
            model_name='pageskin',
            name='filesideimage',
        ),
        migrations.RemoveField(
            model_name='pageskin',
            name='infoimagedefault',
        ),
        migrations.RemoveField(
            model_name='pageskin',
            name='infosideimage',
        ),
    ]