# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

admin.site.site_header = " Admin Panal"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Panal"

admin.site.register(Post)

# Register your models here.
