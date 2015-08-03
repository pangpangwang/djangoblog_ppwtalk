# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150306_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(default=b'write your abstract here', help_text=' ', verbose_name='Abstract'),
            preserve_default=True,
        ),
    ]
