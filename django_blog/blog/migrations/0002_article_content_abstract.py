# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_abstract',
            field=models.TextField(default=b'null', help_text=' ', max_length=255, verbose_name='Abstract'),
            preserve_default=True,
        ),
    ]
