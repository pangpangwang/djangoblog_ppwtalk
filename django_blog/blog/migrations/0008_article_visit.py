# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='visit',
            field=models.IntegerField(default=0, verbose_name='Visit'),
            preserve_default=True,
        ),
    ]
