# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('mvid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('release', models.DateTimeField()),
                ('country', models.CharField(max_length=200)),
                ('run_time', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=50)),
                ('colour', models.BooleanField(default=True)),
                ('rating', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=0)),
                ('body', models.TextField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('dob', models.DateTimeField()),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('jobtitle', models.CharField(max_length=200)),
                ('rolename', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('sid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('establised', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('movie', models.OneToOneField(to='clone.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(to='clone.People'),
            preserve_default=True,
        ),
    ]
