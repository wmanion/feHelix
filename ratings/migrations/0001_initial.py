# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment', models.TextField()),
                ('overall_rating', models.DecimalField(max_digits=10, decimal_places=9)),
                ('qual_of_doc', models.DecimalField(max_digits=10, decimal_places=9)),
                ('efficacy', models.DecimalField(max_digits=10, decimal_places=9)),
                ('usability', models.DecimalField(max_digits=10, decimal_places=9)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('link', models.TextField()),
                ('overall_score', models.DecimalField(max_digits=10, decimal_places=9)),
                ('qual_of_doc', models.DecimalField(max_digits=10, decimal_places=9)),
                ('efficacy', models.DecimalField(max_digits=10, decimal_places=9)),
                ('usability', models.DecimalField(max_digits=10, decimal_places=9)),
                ('free', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('review_count', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ToolCat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cat_id', models.ForeignKey(to='ratings.Category')),
                ('tool_id', models.ForeignKey(to='ratings.Tool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='tool_id',
            field=models.ForeignKey(to='ratings.Tool'),
            preserve_default=True,
        ),
    ]
