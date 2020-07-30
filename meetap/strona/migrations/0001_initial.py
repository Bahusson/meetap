# Generated by Django 3.0.3 on 2020-07-30 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_pl', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('pubdate', models.CharField(max_length=200)),
                ('pubdate_pl', models.CharField(max_length=200, null=True)),
                ('pubdate_en', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200)),
                ('body_pl', models.CharField(max_length=200, null=True)),
                ('body_en', models.CharField(max_length=200, null=True)),
                ('image', models.CharField(max_length=200)),
                ('image_pl', models.CharField(max_length=200, null=True)),
                ('image_en', models.CharField(max_length=200, null=True)),
                ('video', models.CharField(max_length=200)),
                ('video_pl', models.CharField(max_length=200, null=True)),
                ('video_en', models.CharField(max_length=200, null=True)),
                ('lastmod', models.CharField(max_length=200)),
                ('lastmod_pl', models.CharField(max_length=200, null=True)),
                ('lastmod_en', models.CharField(max_length=200, null=True)),
                ('by', models.CharField(max_length=200)),
                ('by_pl', models.CharField(max_length=200, null=True)),
                ('by_en', models.CharField(max_length=200, null=True)),
                ('blog', models.CharField(max_length=200)),
                ('blog_pl', models.CharField(max_length=200, null=True)),
                ('blog_en', models.CharField(max_length=200, null=True)),
                ('new', models.CharField(max_length=200)),
                ('new_pl', models.CharField(max_length=200, null=True)),
                ('new_en', models.CharField(max_length=200, null=True)),
                ('change', models.CharField(max_length=200)),
                ('change_pl', models.CharField(max_length=200, null=True)),
                ('change_en', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_flag', models.ImageField(upload_to='images')),
                ('lang_flag_pl', models.ImageField(null=True, upload_to='images')),
                ('lang_flag_en', models.ImageField(null=True, upload_to='images')),
                ('headtitle', models.CharField(max_length=200)),
                ('headtitle_pl', models.CharField(max_length=200, null=True)),
                ('headtitle_en', models.CharField(max_length=200, null=True)),
                ('mainpage', models.CharField(max_length=200)),
                ('mainpage_pl', models.CharField(max_length=200, null=True)),
                ('mainpage_en', models.CharField(max_length=200, null=True)),
                ('information', models.CharField(max_length=200)),
                ('information_pl', models.CharField(max_length=200, null=True)),
                ('information_en', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200)),
                ('contact_pl', models.CharField(max_length=200, null=True)),
                ('contact_en', models.CharField(max_length=200, null=True)),
                ('logout', models.CharField(max_length=200)),
                ('logout_pl', models.CharField(max_length=200, null=True)),
                ('logout_en', models.CharField(max_length=200, null=True)),
                ('news', models.CharField(max_length=200)),
                ('news_pl', models.CharField(max_length=200, null=True)),
                ('news_en', models.CharField(max_length=200, null=True)),
                ('login', models.CharField(max_length=200)),
                ('login_pl', models.CharField(max_length=200, null=True)),
                ('login_en', models.CharField(max_length=200, null=True)),
                ('panel_user', models.CharField(max_length=200)),
                ('panel_user_pl', models.CharField(max_length=200, null=True)),
                ('panel_user_en', models.CharField(max_length=200, null=True)),
                ('panel_council', models.CharField(max_length=200)),
                ('panel_council_pl', models.CharField(max_length=200, null=True)),
                ('panel_council_en', models.CharField(max_length=200, null=True)),
                ('panel_staff', models.CharField(max_length=200)),
                ('panel_staff_pl', models.CharField(max_length=200, null=True)),
                ('panel_staff_en', models.CharField(max_length=200, null=True)),
                ('backtouserpanel', models.CharField(max_length=200)),
                ('backtouserpanel_pl', models.CharField(max_length=200, null=True)),
                ('backtouserpanel_en', models.CharField(max_length=200, null=True)),
                ('see_more', models.CharField(max_length=200)),
                ('see_more_pl', models.CharField(max_length=200, null=True)),
                ('see_more_en', models.CharField(max_length=200, null=True)),
                ('editme', models.CharField(max_length=200)),
                ('editme_pl', models.CharField(max_length=200, null=True)),
                ('editme_en', models.CharField(max_length=200, null=True)),
                ('faq', models.CharField(max_length=200)),
                ('faq_pl', models.CharField(max_length=200, null=True)),
                ('faq_en', models.CharField(max_length=200, null=True)),
                ('settings', models.CharField(max_length=200)),
                ('settings_pl', models.CharField(max_length=200, null=True)),
                ('settings_en', models.CharField(max_length=200, null=True)),
                ('myprofile', models.CharField(max_length=200)),
                ('myprofile_pl', models.CharField(max_length=200, null=True)),
                ('myprofile_en', models.CharField(max_length=200, null=True)),
                ('events', models.CharField(max_length=200)),
                ('events_pl', models.CharField(max_length=200, null=True)),
                ('events_en', models.CharField(max_length=200, null=True)),
                ('friends', models.CharField(max_length=200)),
                ('friends_pl', models.CharField(max_length=200, null=True)),
                ('friends_en', models.CharField(max_length=200, null=True)),
                ('rules', models.CharField(max_length=200)),
                ('rules_pl', models.CharField(max_length=200, null=True)),
                ('rules_en', models.CharField(max_length=200, null=True)),
                ('register', models.CharField(max_length=50)),
                ('register_pl', models.CharField(max_length=50, null=True)),
                ('register_en', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageSkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themetitle', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('blogimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('infoimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('fileimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('infosideimage', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('filesideimage', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('welcomebanner', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('welcomebanner_small', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('eskslogo_main', models.ImageField(blank=True, null=True, upload_to='skins')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='RegNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50, null=True)),
                ('password_pl', models.CharField(max_length=50, null=True)),
                ('password_en', models.CharField(max_length=50, null=True)),
                ('re_password', models.CharField(max_length=50, null=True)),
                ('re_password_pl', models.CharField(max_length=50, null=True)),
                ('re_password_en', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('name_pl', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('email_pl', models.CharField(max_length=50, null=True)),
                ('email_en', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50)),
                ('gender_pl', models.CharField(max_length=50, null=True)),
                ('gender_en', models.CharField(max_length=50, null=True)),
                ('age', models.CharField(max_length=50)),
                ('age_pl', models.CharField(max_length=50, null=True)),
                ('age_en', models.CharField(max_length=50, null=True)),
                ('agree_to_rules', models.CharField(max_length=50)),
                ('agree_to_rules_pl', models.CharField(max_length=50, null=True)),
                ('agree_to_rules_en', models.CharField(max_length=50, null=True)),
                ('male', models.CharField(max_length=50)),
                ('male_pl', models.CharField(max_length=50, null=True)),
                ('male_en', models.CharField(max_length=50, null=True)),
                ('female', models.CharField(max_length=50)),
                ('female_pl', models.CharField(max_length=50, null=True)),
                ('female_en', models.CharField(max_length=50, null=True)),
                ('other', models.CharField(max_length=50)),
                ('other_pl', models.CharField(max_length=50, null=True)),
                ('other_en', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_pl', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('pubdate', models.DateTimeField(blank=True, null=True)),
                ('body', models.TextField()),
                ('body_pl', models.TextField(null=True)),
                ('body_en', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image_pl', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image_en', models.ImageField(blank=True, null=True, upload_to='images')),
                ('video', models.CharField(blank=True, max_length=500, null=True)),
                ('video_pl', models.CharField(blank=True, max_length=500, null=True)),
                ('video_en', models.CharField(blank=True, max_length=500, null=True)),
                ('lastmod', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pubdate'],
            },
        ),
    ]
