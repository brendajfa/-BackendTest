# -BackendTest

<div align="justify">

We need to define an API for our media platform, which allows us to display contents
following a hierarchical structure.
A Content can contain files (such as videos, pdfs, or text), a set of arbitrary metadata
associated with the content (content descriptions, authors, genre, etc.) and a rating
value which is a decimal number between 0 and 10.
See the following example of a Content, corresponding to an episode of a TV series.

<p align="center">
    <img src="Images/InfoRagnar.png">
</p>



We organize the contents in the platform through the use of Channels. A Channel
stores the hierarchical structure and has a title, a language, and a picture. A channel
can contain references to either other channels or contents. If a channel has
subchannels, it cannot have any content underneath, conversely, if a channel has
contents, it cannot have any subchannel underneath. A channel must have at least
one content or one subchannel.

In the following images, you can see an example of the channels that could be provided
by your API.

<p align="center">
    <img src="Images/Example.png">
</p>

The rating of a channel is the average of the ratings of all the channels underneath, if
the channel has no subchannels its rating is the average of the ratings of its contents. If
a channel has no contents, it does not affect the ratings of its parent since its value is
undefined.
Channels can’t store this rating directly (because the structure can change at any time), so we need a way to compute it from the content structure behind them.

</div>


# Requirements

<div align="justify">

The requirements we ask for this test are:

* Create a Django project to define an API
* Define models to represent the structure explained above
* Create a management command to efficiently calculate the ratings of every
* annel and export them in a csv file sorted by rating (i.e. the highest rated
* annels on top). The csv contains two columns: <channel title>, <average
* ting>
* Create endpoints to retrieve the channels, their subchannels and its contents
* Add unit tests to test the channel rating algorithm


Get bonus points for:
* Adding Groups to the channels. Considering that each channel can belong to multiple groups.
  
> Allow filtering by group on Channels API.
Note: Take into account that any channel’s groups set should be included in its parent’s group set

* High test coverage through unit tests
* Usage of docker to run the services
* Addition of type annotations (bonus for passing strict mypy type checks)
* Adding CI/CD (Gitlab CI is preferred, but you can use anything you want)
You can use any libraries, DBMS or tools you need to accomplish the task.
We encourage you to define a readme file with some explanations about your solution.

</div>

# Create a Django project

```bash
django-admin startproject immfly_django
cd immfly_django
python manage.py startapp myapi
```


# Execution procedure

```bash
cd  "C:\Users\brend\OneDrive\Escritorio\Formación\Immfly\-BackendTest"
conda create --name immfly python=3.8
conda activate immfly
pip install -r requirements.txt 


# django-admin startproject immfly_django
# cd immfly_django
# python manage.py startapp myapi

# Run django environment
python manage.py runserver

```


```bash
(immfly) C:\Users\brend\OneDrive\Escritorio\Formación\Immfly\-BackendTest\immfly_django>python manage.py check myapi
System check identified no issues (0 silenced).

(immfly) C:\Users\brend\OneDrive\Escritorio\Formación\Immfly\-BackendTest\immfly_django>python manage.py makemigrations
Migrations for 'myapi':
  myapi\migrations\0001_initial.py
    - Create model Channel
    - Create model SubChannel
    - Create model TVShow
    - Create model Press_and_Magazines
    - Create model Music_and_Podcasts
    - Create model Movies
    - Create model LifestyleContent
    - Create model Kids
    - Create model Games
    - Create model Audible

## To get the SQL commands
>> python manage.py sqlmigrate myapi 0001


python manage.py makemigrations
python manage.py migrate --run-syncdb
```


## python manage.py shell

```Python

from my_api.models import Content, Channel, SubChannel, TVSHOW, AUDIBLE, MOVIES, LIFESTYLE, MUSIC_PODCASTS, KIDS, PRESS_MAGAZINES, GAMES, RatingComputing

from numpy import mean
import numpy as np
import pandas as pd

channels_list = Channel.objects.all()
channels_list.delete()
audible_channel = Channel.objects.create(title='AUDIBLE')
movies_channel = Channel.objects.create(title='MOVIES')
tv_shows_channel = Channel.objects.create(title='TV SHOWS')
lifestyle_channel = Channel.objects.create(title='LIFESTYLE')
msc_pdcst_channel = Channel.objects.create(title='MUSIC & PODCASTS')
kids_channel = Channel.objects.create(title='KIDS')
press_mgzn_channel = Channel.objects.create(title='PRESS & MAGAZINES')
games_channel = Channel.objects.create(title='GAMES')

channel_ex = Channel.objects.create(title='channel example')

mario_bros = GAMES.objects.create(title='Mario Bros', parent_channel=games_channel)
# mario_bros.parent_channel.set(channel_ex)



soulmates = TVSHOW.objects.create(title='SOULMATES', parent_channel=tv_shows_channel)
the_handmaids_tale = TVSHOW.objects.create(title="THE HANDMAID'S TALE", parent_channel=tv_shows_channel)
vikings = TVSHOW.objects.create(title='VIKINGS', parent_channel=tv_shows_channel)
blindspot = TVSHOW.objects.create(title='BLINDSPOT', parent_channel=tv_shows_channel)
you = TVSHOW.objects.create(title='YOU', parent_channel=tv_shows_channel)

tv_shows_list = TVSHOW.objects.all()
metadata_s1_e1 = {
    'title':'S1:E1 Rites of Passage',
    'lan':['Spanish','French','English'],
    'sub':['Spanish','Portuguese'],
    'description': "DESCRIPTION 1 ...."
    }

metadata_s1_e2 = {
    'title':'S1:E2 Wrath of the Northmen',
    'lan':['Spanish','French','English'],
    'sub':['Spanish','Portuguese'],
    'description': "DESCRIPTION 2 ...."
    }

# metadata_g_1 = {
#     'game':'Mario Bros',
#     'description': "DESCRIPTION MARIO BROS ...."
#     }

# metadata_g_2 = {
#     'game':'Snake',
#     'description': "DESCRIPTION SNAKE ...."
#     }

vikings_s1_e1 = Content.objects.create(metadata= metadata_s1_e1, rating = 8, tvshow_ch = vikings)
vikings_s1_e2 = Content.objects.create(metadata= metadata_s1_e2, rating = 7, tvshow_ch = vikings)

content_1 = Content.objects.create(rating = 2, tvshow_ch = soulmates)
content_2 = Content.objects.create(rating = 5, tvshow_ch = the_handmaids_tale)
content_3 = Content.objects.create(rating = 3, tvshow_ch = blindspot)
content_4 = Content.objects.create(rating = 9, tvshow_ch = you)

# vikings_contents = vikings.objects.all()
# vikings_contents

tv_shows_list = TVSHOW.objects.all()
# tv_shows_list.delete()
tv_shows_list

channels_list = Channel.objects.all()
# channels_list.delete()
channels_list


def average_rating(ObjectChannel_list):

    results = {}    
    for objectChannel in ObjectChannel_list:
        object_content = objectChannel.content.all()
        ratings = [content.rating for content in object_content]
        print(object_content)
        if ratings ==[]:
            results[objectChannel.title] = 0
        else:
            # print(ratings)
            # print(sum(ratings)/len(ratings))
            results[objectChannel.title] = sum(ratings)/len(ratings)
            # print(object_content)
            # print(ratings) 
    return results

r={}
r["TV SHOWS"] = average_rating(TVSHOW.objects.all())
r["AUDIBLE"] = average_rating(AUDIBLE.objects.all())
r["PRESS AND MAGAZINES"] = average_rating(PRESS_MAGAZINES.objects.all())
r["KIDS"] = average_rating(KIDS.objects.all())
r["MUSIC AND PODCASTS"] = average_rating(MUSIC_PODCASTS.objects.all())
r["LIFESTYLE"] = average_rating(LIFESTYLE.objects.all())
r["MOVIES"] = average_rating(MOVIES.objects.all())
r["GAMES"] = average_rating(GAMES.objects.all())
r


for channel, info in r.items():
    ratings = [*info.values()]
    avg_rating = sum(ratings)/len(ratings) if len(ratings)!=0 else 0.0
    r[channel] = avg_rating


df= pd.DataFrame([[key, r[key]] for key in r.keys()], columns=['Channels', 'Rating'])
df.to_csv("channels_rating.csv")

# channels_id = Channel.objects.values('id')

# contents_list = Content.objects.all()
# contents_list

# for content_id in range(9,11):
#     content = Channel.objects.get(id=content_id)
#     content.delete()

# channels_list
# for channel in channels_list:
#     avg_rating = channel.contents.filter(rating__isnull=False).aggregate(Avg('rating'))['rating__avg']
#     print(avg_rating)
#     channel.avg_rating = avg_rating
#     print(channel.avg_rating)
#     channel.save()
#     print(f'Successfully updated rating for channel {channel.id}')




---
from my_api.models import Content, Channel, SubChannel, TVSHOW, AUDIBLE, MOVIES, LIFESTYLE, MUSIC_PODCASTS, KIDS, PRESS_MAGAZINES, GAMES
audible = Channel.objects.create(title='AUDIBLE')
vikings = AUDIBLE.objects.create(title='VIKINGS', parent_channel=audible)
vikings_s1_e1 = Content.objects.create(rating = 8, audible_ch = vikings)
vikings_s1_e2 = Content.objects.create(rating = 7, audible_ch = vikings)


vikings_contents = vikings.audible.all()  # Get all the contents related to vikings
ratings = [content.rating for content in vikings_contents]  # Extract the rating of each content
print(ratings)  # Print the list of ratings
```