# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
