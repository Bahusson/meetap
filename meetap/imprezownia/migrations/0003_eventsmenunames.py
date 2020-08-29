# Generated by Django 2.2.4 on 2020-08-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprezownia', '0002_auto_20200809_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsMenuNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintitle', models.CharField(max_length=50)),
                ('maintitle_pl', models.CharField(max_length=50, null=True)),
                ('maintitle_en', models.CharField(max_length=50, null=True)),
                ('new_event', models.CharField(max_length=50)),
                ('new_event_pl', models.CharField(max_length=50, null=True)),
                ('new_event_en', models.CharField(max_length=50, null=True)),
                ('my_events', models.CharField(max_length=50)),
                ('my_events_pl', models.CharField(max_length=50, null=True)),
                ('my_events_en', models.CharField(max_length=50, null=True)),
                ('edit_event', models.CharField(max_length=50)),
                ('edit_event_pl', models.CharField(max_length=50, null=True)),
                ('edit_event_en', models.CharField(max_length=50, null=True)),
                ('search_events', models.CharField(max_length=50)),
                ('search_events_pl', models.CharField(max_length=50, null=True)),
                ('search_events_en', models.CharField(max_length=50, null=True)),
                ('my_teplates', models.CharField(max_length=50)),
                ('my_teplates_pl', models.CharField(max_length=50, null=True)),
                ('my_teplates_en', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'EventsMenuNames',
            },
        ),
    ]