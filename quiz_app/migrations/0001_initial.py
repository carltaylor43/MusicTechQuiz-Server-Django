# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, to='quiz_app.BaseModel', serialize=False)),
                ('title', models.CharField(max_length=120, default='')),
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
                ('basemodel_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, to='quiz_app.BaseModel', serialize=False)),
                ('title', models.CharField(max_length=120, default='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=('quiz_app.basemodel',),
        ),
    ]
