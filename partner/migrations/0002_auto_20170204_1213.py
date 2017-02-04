# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='address',
            field=models.CharField(max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='contact',
            field=models.CharField(max_length=50, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(verbose_name='상세 소개'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=50, verbose_name='업체 이름'),
        ),
    ]
