# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-20 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businesspic', models.ImageField(blank=True, upload_to='images/')),
                ('businessname', models.CharField(max_length=30)),
                ('businessemail', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoodpic', models.ImageField(blank=True, upload_to='images')),
                ('hoodname', models.CharField(max_length=30)),
                ('numberofpeople', models.IntegerField(blank=True, default=0)),
                ('hoodlocation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newspic', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField()),
                ('newsloaction', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='images/')),
                ('email', models.CharField(max_length=60)),
                ('Hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhood.Neighborhood')),
                ('editor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nhood.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
