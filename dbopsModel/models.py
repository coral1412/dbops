#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime

import base64
from Crypto.Cipher import AES
from Crypto import Random
BS = 16
aes_key = 'This is a key123'
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

# from Crypto.Cipher import AES
# from DBOPS.settings import SECRET_KEY
# from binascii import b2a_hex, a2b_hex

# Create your models here.
class dbuserinfo(models.Model):
    id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=30,verbose_name="项目名字",null=True)
    user_name = models.CharField(max_length=50,verbose_name="DB对接人")
    dbhost=models.CharField(max_length=20,verbose_name="数据库IP",null=True)
    dbname = models.CharField(max_length=32, verbose_name="DBNAME")
    ser_name=models.CharField(max_length=20,verbose_name="DB用户名")
    ser_passwd=models.CharField(max_length=16,verbose_name="DB用户密码")
    grant_host = models.CharField(max_length=20,verbose_name="DB授权IP/IP网段")
    dbprivileges=models.CharField(max_length=30,verbose_name="DB授权详情")
    createtime=models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    updatetime=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    adduser=models.CharField(max_length=20,verbose_name="添加人",null=True)
    comment=models.CharField(max_length=50,verbose_name="预发布/生产")
    # def set_db_password(self, ser_passwd):
    #     raw = pad(ser_passwd)
    #     iv = Random.new().read(AES.block_size)
    #     cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    #     self.ser_passwd = base64.b64encode(iv + cipher.encrypt(raw))
    # def get_db_password(self):
    #     enc = base64.b64decode(self.ser_passwd)
    #     iv = enc[:16]
    #     cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    #     return unpad(cipher.decrypt(enc[16:]))

    # class Prpcrypt(object):
    # def __init__(self):
    #     # self.key ="0g7h5$ppy_o4fr6&58)*a(mjp6fn(8%gmm@j4%ocqw+po&ju7_"
    #     self.key = SECRET_KEY
    #     self.mode = AES.MODE_CBC
    #
    # def encrypt(self, ser_passwd):
    #     cryptor = AES.new(self.key[:16], self.mode, b'0000000000000000')
    #     pad_it = lambda self, s: s + (16 - len(s) % 16) * '\0'
    #     return b2a_hex(cryptor.encrypt(pad_it(self, ser_passwd)))
    #
    # def decrypt(self, ser_passwd):
    #     cryptor = AES.new(self.key[:16], self.mode, b'0000000000000000')
    #     plain_text = cryptor.decrypt(a2b_hex(ser_passwd))
    #     return plain_text.decode().rstrip('\0')

    def __unicode__(self):
        return self.project_name
    class Meta:
        verbose_name="DB用户记录表"
        verbose_name_plural="DB用户表"

