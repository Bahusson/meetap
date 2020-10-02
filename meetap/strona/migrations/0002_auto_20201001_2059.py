# Generated by Django 3.1 on 2020-10-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_S_A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(auto_created=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('title_pl', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_under_menu', models.BooleanField(default=True)),
                ('is_on_list', models.BooleanField(default=True)),
                ('link_external', models.TextField(blank=True, null=True)),
                ('link_external_pl', models.TextField(blank=True, null=True)),
                ('link_external_en', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image_pl', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image_en', models.ImageField(blank=True, null=True, upload_to='images')),
                ('body', models.TextField(blank=True, null=True)),
                ('body_pl', models.TextField(blank=True, null=True)),
                ('body_en', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Public Service Announcements',
                'ordering': ['position'],
            },
        ),
        migrations.AlterModelOptions(
            name='blognames',
            options={'verbose_name_plural': 'Blog Names'},
        ),
        migrations.AlterModelOptions(
            name='pageskin',
            options={'ordering': ['position'], 'verbose_name_plural': 'Page Skins'},
        ),
        migrations.AlterModelOptions(
            name='profilenames',
            options={'verbose_name_plural': 'Profile Names'},
        ),
        migrations.AlterModelOptions(
            name='regnames',
            options={'verbose_name_plural': 'Registry Names'},
        ),
    ]