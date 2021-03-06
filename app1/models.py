# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Post(models.Model):
    post = models.TextField(max_length=500)
    image = models.ImageField(upload_to= 'meida')
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(Post, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Post, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return self.post




# Create your models here.
