from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Game(models.Model):
    owner = models.ForeignKey(User)
    url = models.CharField(max_length=40, unique = True)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    tile2 = ResizedImageField(upload_to='tiles')
    tile4 = ResizedImageField(upload_to='tiles')
    tile8 = ResizedImageField(upload_to='tiles')
    tile16 = ResizedImageField(upload_to='tiles')
    tile32 = ResizedImageField(upload_to='tiles')
    tile64 = ResizedImageField(upload_to='tiles')
    tile128 = ResizedImageField(upload_to='tiles')
    tile256 = ResizedImageField(upload_to='tiles')
    tile512 = ResizedImageField(upload_to='tiles')
    tile1024 = ResizedImageField(upload_to='tiles')
    tile2048 = ResizedImageField(upload_to='tiles')

    def __unicode__(self):
        return self.name