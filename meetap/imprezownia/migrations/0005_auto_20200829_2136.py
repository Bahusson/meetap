# Generated by Django 3.1 on 2020-08-29 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imprezownia', '0004_auto_20200811_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyDivider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_pl', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('descr', models.CharField(blank=True, max_length=500, null=True)),
                ('descr_pl', models.CharField(blank=True, max_length=500, null=True)),
                ('descr_en', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='body_en',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='body_pl',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='other_preferences_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='other_preferences_pl',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_pl', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('role_descr', models.CharField(blank=True, max_length=600, null=True)),
                ('role_descr_pl', models.CharField(blank=True, max_length=600, null=True)),
                ('role_descr_en', models.CharField(blank=True, max_length=600, null=True)),
                ('alt_user', models.CharField(blank=True, max_length=150, null=True)),
                ('tax_free', models.BooleanField(default=False)),
                ('aux_coordinator', models.BooleanField(default=False)),
                ('assigned_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('from_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imprezownia.partydivider')),
            ],
        ),
        migrations.CreateModel(
            name='TaxPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_pl', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('descr', models.CharField(blank=True, max_length=200, null=True)),
                ('descr_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('descr_en', models.CharField(blank=True, max_length=200, null=True)),
                ('tax_type', models.PositiveSmallIntegerField(choices=[(0, 'i'), (1, 'lub'), (2, 'opcjonalnie'), (3, 'każdy')], default=0)),
                ('from_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imprezownia.event')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_pl', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('descr', models.CharField(blank=True, max_length=500, null=True)),
                ('descr_pl', models.CharField(blank=True, max_length=500, null=True)),
                ('descr_en', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('from_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imprezownia.taxpanel')),
            ],
        ),
        migrations.AddField(
            model_name='partydivider',
            name='from_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imprezownia.event'),
        ),
    ]