# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150306_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content_abstract',
            new_name='abstract',
        ),
    ]
