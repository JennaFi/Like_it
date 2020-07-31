from django.contrib import admin
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from pet_likes.models import Like


class Pet(models.Model):

    name = models.CharField(max_length=150, db_index=True)
    size = models.CharField('Size', default='', help_text='weight, kg', max_length=50)
    breed = models.CharField(default="Mongrel", max_length=100)
    body = models.CharField(max_length=140)
    age = models.CharField('Age', default='', help_text='y.o.', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'size', 'body')
    list_filter = ('name', 'breed',)

    fields = ('name', 'breed', 'age', 'size',  'body',  'visible', )
