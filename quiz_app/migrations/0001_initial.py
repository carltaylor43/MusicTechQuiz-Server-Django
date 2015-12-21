# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, to='quiz_app.BaseModel', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(default='', max_length=120)),
                ('order_number', models.IntegerField()),
            ],
            options={
                'ordering': ('order_number',),
            },
            bases=('quiz_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, to='quiz_app.BaseModel', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(default='', max_length=120)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=('quiz_app.basemodel',),
        ),
    ]
