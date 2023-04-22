
from django.db import models
from numpy import mean
from django.core.exceptions import ValidationError


from django.db import models

class Channel(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     # Custom save method to enforce the rule that a channel must have at least one content or one subchannel
    #     if self.contents.count() == 0 and self.subchannels.count() == 0:
    #         raise ValueError("A channel must have at least one content or one subchannel")
    #     elif self.contents.count() != 0 and self.subchannels.count() != 0:
    #         raise ValueError("A channel must have just contents or subchannels")
    #     super().save(*args, **kwargs)


class SubChannel(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='subchannel')

    def __str__(self):
        return self.title

class AUDIBLE(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='audible')
    # contents = models.ManyToManyField('Content', related_name='audible', blank=True)

    def __str__(self):
        return self.title
    
# class AUDIBLE_(Channel):
#     title = models.CharField(max_length=50)
#     language = models.CharField(max_length=100)
#     picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
#     parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='audible')
#     contents = models.ManyToManyField('Content', related_name='audible', blank=True)

#     def __str__(self):
#         return self.title

class MOVIES(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    # contents = models.ManyToManyField('Content', related_name='movies', blank=True)

    def __str__(self):
        return self.title
    
class TVSHOW(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='tv_show')
    # contents = models.ManyToManyField('Content', related_name='tv_show', blank=True)

    def __str__(self):
        return self.title
    
class LIFESTYLE(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='lifestyle')
    # contents = models.ManyToManyField('Content', related_name='lifestyle', blank=True)

    def __str__(self):
        return self.title
    
class MUSIC_PODCASTS(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='music_podcasts')
    # contents = models.ManyToManyField('Content', related_name='music_podcasts', blank=True)

    def __str__(self):
        return self.title
    
class KIDS(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='kids')
    # contents = models.ManyToManyField('Content', related_name='kids', blank=True)

    def __str__(self):
        return self.title
    
class PRESS_MAGAZINES(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='press_magazines')
    # contents = models.ManyToManyField('Content', related_name='press_magazines', blank=True)

    def __str__(self):
        return self.title
    
class GAMES(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='channel_pictures', null=True, blank=True)
    
    parent_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='games')
    # contents = models.ManyToManyField('Content', related_name='games', blank=True)


    def __str__(self):
        return self.title
    

class Content(models.Model): # Content, corresponding to an episode of a TV series
    metadata = models.JSONField(default=dict)
    file = models.FileField(upload_to='uploads/')
    rating = models.IntegerField()

    # audible_ch = models.ForeignKey('AUDIBLE', on_delete=models.CASCADE, null=True, blank=True, related_name='audible')
    # press_ch = models.ForeignKey('PRESS_MAGAZINES', on_delete=models.CASCADE, null=True, blank=True, related_name='press')
    # kids_ch = models.ForeignKey('KIDS', on_delete=models.CASCADE, null=True, blank=True, related_name='kids')
    # music_ch = models.ForeignKey('MUSIC_PODCASTS', on_delete=models.CASCADE, null=True, blank=True, related_name='music')
    # lifestyle_ch = models.ForeignKey('LIFESTYLE', on_delete=models.CASCADE, null=True, blank=True, related_name='lifestyle')
    # tvshow_ch = models.ForeignKey('TVSHOW', on_delete=models.CASCADE, null=True, blank=True, related_name='tvshow')
    # movies_ch = models.ForeignKey('MOVIES', on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    # games_ch = models.ForeignKey('GAMES', on_delete=models.CASCADE, null=True, blank=True, related_name='games')

    
    audible_ch = models.ForeignKey('AUDIBLE', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    press_ch = models.ForeignKey('PRESS_MAGAZINES', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    kids_ch = models.ForeignKey('KIDS', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    music_ch = models.ForeignKey('MUSIC_PODCASTS', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    lifestyle_ch = models.ForeignKey('LIFESTYLE', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    tvshow_ch = models.ForeignKey('TVSHOW', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    movies_ch = models.ForeignKey('MOVIES', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
    games_ch = models.ForeignKey('GAMES', on_delete=models.CASCADE, null=True, blank=True, related_name='content')
        
    def __str__(self):
        return str(self.rating)
    # tvshow = models.ForeignKey(TV_Show, on_delete=models.CASCADE, related_name='episodes')


def average_rating_models(ObjectChannel_list):

    results = {}    
    for objectChannel in ObjectChannel_list:
        object_content = objectChannel.content.all()
        ratings = [content.rating for content in object_content]
        print(object_content)
        if ratings ==[]:
            results[objectChannel.title] = 0
        else:
            results[objectChannel.title] = sum(ratings)/len(ratings)
    return results

