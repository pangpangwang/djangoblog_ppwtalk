# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150306_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(default=b'write your abstract here', help_text=' ', max_length=100, verbose_name='Abstract'),
            preserve_default=True,
        ),
    ]
