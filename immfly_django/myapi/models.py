
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class SubChannel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent_channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TVShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Kids(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class LifestyleContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Audible(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Music_and_Podcasts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Press_and_Magazines(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Games(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subchannel = models.ForeignKey(SubChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
