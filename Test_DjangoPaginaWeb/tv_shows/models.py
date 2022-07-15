from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        #Validamos que la cantidad de carácteres del título sea al menos 2 letras.
        if len(postData['title'].strip()) < 2:
            errors['title'] = 'The title must be at least 2 characters'
            
        if len(postData['title'].strip()) > 101:
            errors['title'] = 'The title must be at less than 100 characters'

        if len(postData['network']) < 1:
            errors['network'] = 'The network must be selected at least once'

        if len(postData['description'].strip()) < 10:
            errors['description'] = 'The description must be at least 10 characters'
        
        return errors


class Network(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    network = models.ForeignKey(Network, on_delete = models.CASCADE)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title



