# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.TextField(default=''),
        ),
    ]
