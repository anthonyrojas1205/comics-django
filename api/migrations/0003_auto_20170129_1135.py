# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-29 11:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160525_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='condition_rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10.0, '10.0 Gem Mint'), (9.9, '9.9 Mint'), (9.8, '9.8 Near Mint/Mint'), (9.6, '9.6 Near Mint +'), (9.4, '9.4 Near Mint'), (9.2, '9.2 Near Mint -'), (9.0, '9.0 Very Fine/Near Mint'), (8.5, '8.5 Very Fine +'), (8.0, '8.0 Very Fine'), (7.5, '7.5 Very Fine -'), (7.0, '7.0 Fine/Very Fine'), (6.5, '6.5 Fine +'), (6.0, '6.0 Fine'), (5.5, '5.5 Fine -'), (5.0, '5.0 Very Good/Fine'), (4.5, '4.5 Very Good +'), (4.0, '4.0 Very Good'), (3.5, '3.5 Very Good -'), (3.0, '3.0 Good/Very Good'), (2.5, '2.5 Good +'), (2.0, '2.0 Good'), (1.8, '1.8 Good -'), (1.5, '1.5 Fair/Good'), (1.0, '1.0 Fair'), (0.5, '.5 Poor'), (0, 'NG')], null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='gcdindiciapublisher',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GCDCountry'),
        ),
        migrations.AlterField(
            model_name='gcdpublisher',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GCDCountry'),
        ),
        migrations.AlterField(
            model_name='gcdseries',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GCDCountry'),
        ),
        migrations.AlterField(
            model_name='gcdseries',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GCDLanguage'),
        ),
    ]
