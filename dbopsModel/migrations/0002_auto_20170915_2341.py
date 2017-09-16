# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-15 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbopsModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='createtime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='project_name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u9879\u76ee\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='comment',
            field=models.CharField(max_length=50, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dbname',
            field=models.CharField(max_length=32, verbose_name='dbname'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dbprivileges',
            field=models.CharField(max_length=30, verbose_name='\u6388\u6743\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='grant_host',
            field=models.CharField(max_length=20, verbose_name='db\u6388\u6743IP/IP\u7f51\u6bb5'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ser_name',
            field=models.CharField(max_length=20, verbose_name='db\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ser_passwd',
            field=models.CharField(max_length=16, verbose_name='db\u7528\u6237\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='db\u5bf9\u63a5\u4eba'),
        ),
    ]