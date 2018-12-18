# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=20)),
            ],
        ),
    ]
