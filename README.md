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
```