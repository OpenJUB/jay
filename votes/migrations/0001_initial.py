# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('picture_url', models.URLField(blank=True)),
                ('personal_link', models.URLField(blank=True)),
                ('link_name', models.CharField(max_length=16, blank=True)),
                ('count', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PassiveVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('num_voters', models.IntegerField()),
                ('num_eligible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('open_time', models.DateTimeField(blank=True, null=True)),
                ('close_time', models.DateTimeField(blank=True, null=True)),
                ('public_time', models.DateTimeField(blank=True, null=True)),
                ('stage', models.CharField(max_length=1, default='I', choices=[('I', 'Init'), ('S', 'Staged'), ('O', 'Open'), ('C', 'Close'), ('P', 'Results public')])),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('machine_name', models.SlugField(max_length=64)),
                ('auto_open_options', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('min_votes', models.IntegerField()),
                ('max_votes', models.IntegerField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('filter', models.ForeignKey(null=True, to='filters.UserFilter')),
                ('status', models.OneToOneField(to='votes.Status')),
                ('system', models.ForeignKey(to='settings.VotingSystem')),
            ],
        ),
        migrations.AddField(
            model_name='passivevote',
            name='vote',
            field=models.OneToOneField(to='votes.Vote'),
        ),
        migrations.AddField(
            model_name='option',
            name='vote',
            field=models.ForeignKey(to='votes.Vote'),
        ),
        migrations.AddField(
            model_name='activevote',
            name='vote',
            field=models.ForeignKey(to='votes.Vote'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('system', 'machine_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set([('vote', 'number')]),
        ),
    ]
