# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Target(models.Model):
    user_id = models.IntegerField()

    def __unicode__(self):
        return self.user_id


class Result(models.Model):
    target = models.ForeignKey(Target)
    nickname = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('published date')

    def __unicode__(self):
        return self.content
