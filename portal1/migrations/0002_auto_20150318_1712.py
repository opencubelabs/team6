# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portal1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Coupon',
            new_name='coupon',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='Cost',
        ),
        migrations.RemoveField(
            model_name='events',
            name='Name',
        ),
        migrations.AddField(
            model_name='events',
            name='eventName',
            field=models.CharField(default=b'NIL', max_length=200, choices=[(b'NIL', b'None(Rs.0)'), (b'SH', b'Space Hackathon(Rs.100)'), (b'CS', b'Cansat Seminar(Rs.150'), (b'SW', b'Space Workshops(Rs.200')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='Event',
            field=models.ForeignKey('Events',default=0),
            preserve_default=False,
        ),
    ]
