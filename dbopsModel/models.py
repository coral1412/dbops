#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.hashers import BasePasswordHasher,MD5PasswordHasher
from django.contrib.auth.hashers import mask_hash
import  hashlib
# Create your models here.
class dbuserinfo(models.Model):
    id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=30,verbose_name="项目名字",null=True)
    user_name = models.CharField(max_length=50,verbose_name="DB对接人")
    dbhost=models.CharField(max_length=20,verbose_name="数据库IP",null=True)
    dbname = models.CharField(max_length=32, verbose_name="DBNAME")
    ser_name=models.CharField(max_length=20,verbose_name="DB用户名")
    ser_passwd=models.CharField(max_length=100,verbose_name="DB用户密码")
    grant_host = models.CharField(max_length=20,verbose_name="DB授权IP/IP网段")
    dbprivileges=models.CharField(max_length=30,verbose_name="DB授权详情")
    createtime=models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    updatetime=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    adduser=models.CharField(max_length=20,verbose_name="添加人",null=True)
    comment=models.CharField(max_length=50,verbose_name="预发布/生产")
    # def save(self, *args,**kwargs):
    #     self.ser_passwd=hashlib.sha1(self.ser_passwd+self.user_name).hexdigest()
    #     super(dbuserinfo,self).save(*args,**kwargs)


    def __unicode__(self):
        return self.project_name
    class Meta:
        verbose_name="应用用户表"
        verbose_name_plural="应用用户表"

class dbinfo(models.Model):
    id=models.AutoField(primary_key=True)
    t_project_name=models.CharField(max_length=30,verbose_name="项目名字")
    t_owner=models.CharField(max_length=20,verbose_name="项目负责人")
    t_dbhost=models.CharField(max_length=20,verbose_name="数据库IP")
    t_rootpasswd=models.CharField(max_length=100,verbose_name="root用户密码")
    t_dbs=models.CharField(max_length=64,verbose_name="所含数据库")
    t_createuser=models.CharField(max_length=32,verbose_name="添加人")
    t_createtime=models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    t_updatetime=models.DateTimeField(auto_now=True,verbose_name="更改时间")
    t_comment=models.CharField(max_length=64,verbose_name="注释")
    def __unicode__(self):
        return self.t_project_name
    class Meta:
        verbose_name="生产数据库统计表"
        verbose_name_plural="生产数据库信息统计表"