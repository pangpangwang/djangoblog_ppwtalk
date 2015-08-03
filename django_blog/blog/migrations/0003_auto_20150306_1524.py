# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_content_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_abstract',
            field=models.TextField(default=b'write your abstract here', help_text=' ', max_length=255, verbose_name='Abstract'),
            preserve_default=True,
        ),
    ]
