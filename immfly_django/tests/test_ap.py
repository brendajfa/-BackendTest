import pytest

from my_api.models import Content, Channel, TVSHOW, AUDIBLE, MOVIES, LIFESTYLE, MUSIC_PODCASTS, KIDS, PRESS_MAGAZINES, GAMES

import numpy as np
import pandas as pd

@pytest.mark.django_db
class TestExample:
    def average_rating(self, ObjectChannel_list):

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

    def test_one(self):
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


        mario_bros = GAMES.objects.create(title='Mario Bros', parent_channel=games_channel)


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

        vikings_s1_e1 = Content.objects.create(metadata= metadata_s1_e1, rating = 8, tvshow_ch = vikings)
        vikings_s1_e2 = Content.objects.create(metadata= metadata_s1_e2, rating = 7, tvshow_ch = vikings)

        content_1 = Content.objects.create(rating = 2, tvshow_ch = soulmates)
        content_2 = Content.objects.create(rating = 5, tvshow_ch = the_handmaids_tale)
        content_3 = Content.objects.create(rating = 3, tvshow_ch = blindspot)
        content_4 = Content.objects.create(rating = 9, tvshow_ch = you)

        tv_shows_list = TVSHOW.objects.all()
        # tv_shows_list.delete()
        tv_shows_list

        channels_list = Channel.objects.all()
        # channels_list.delete()
        channels_list




        r={}
        r["TV SHOWS"] = self.average_rating(TVSHOW.objects.all())
        r["AUDIBLE"] = self.average_rating(AUDIBLE.objects.all())
        r["PRESS AND MAGAZINES"] = self.average_rating(PRESS_MAGAZINES.objects.all())
        r["KIDS"] = self.average_rating(KIDS.objects.all())
        r["MUSIC AND PODCASTS"] = self.average_rating(MUSIC_PODCASTS.objects.all())
        r["LIFESTYLE"] = self.average_rating(LIFESTYLE.objects.all())
        r["MOVIES"] = self.average_rating(MOVIES.objects.all())
        r["GAMES"] = self.average_rating(GAMES.objects.all())
        r


        for channel, info in r.items():
            ratings = [*info.values()]
            avg_rating = sum(ratings)/len(ratings) if len(ratings)!=0 else 0.0
            r[channel] = avg_rating


        df= pd.DataFrame([[key, r[key]] for key in r.keys()], columns=['Channels', 'Rating'])
        df.to_csv("channels_rating.csv")