# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200, unique=True)
	author = models.CharField(max_length=100)
