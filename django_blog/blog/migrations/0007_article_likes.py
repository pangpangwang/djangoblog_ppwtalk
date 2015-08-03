# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150306_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Likes'),
            preserve_default=True,
        ),
    ]
