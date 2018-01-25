from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from os import listdir
import os, json, random
from os.path import isfile, join
from django.conf import settings

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
show n pictures randomly
"""


class Constants(BaseConstants):
    name_in_url = 'picturerollerapp'
    players_per_group = None
    mypath = settings.STATICFILES_DIRS[0]
    photos = [f for f in listdir(join(mypath, 'picturerollerapp/photos')) if f.endswith(('.jpg') or ('.jpeg') or ('.png'))]
    num_rounds = len(photos)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.session.get_participants():
                photos = Constants.photos.copy()
                random.shuffle(photos)
                p.vars['photos'] = json.dumps(photos)
        for p in self.get_players():
            p.photos = p.participant.vars['photos']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    photos=models.CharField()

    current_pic=models.CharField()

    happy = models.CharField(
        verbose_name="...happy",
        choices=['0, not happy at all', '1', '2', '3', '4', '5','6','7, extremely happy'],
    )

    angry = models.CharField(
        verbose_name="...angry",
        choices=['0, not angry at all', '1', '2', '3', '4', '5','6','7, extremely angry'],
    )

    fearful = models.CharField(
        verbose_name="...fearful",
        choices=['0, not fearful at all', '1', '2', '3', '4', '5','6','7, extremely fearful'],
    )

    surprised = models.CharField(
        verbose_name="...surprised",
        choices=['0, not surprised at all', '1', '2', '3', '4', '5','6','7, extremely surprised'],
    )

    sad = models.CharField(
        verbose_name="...sad",
        choices=['0, not sad at all', '1', '2', '3', '4', '5','6','7, extremely sad'],
    )

    neutral = models.CharField(
        verbose_name="...neutral",
        choices=['0, not neutral at all', '1', '2', '3', '4', '5','6','7, extremely neutral'],
    )

    looks = models.CharField(
        verbose_name="Good looks?",
        choices=['0, not good looking at all', '1', '2', '3', '4', '5','6','7, extremely good looking'],
    )

    trustworthiness = models.CharField(
        verbose_name="Trustworthiness?",
        choices=['0, not trustworthy at all', '1', '2', '3', '4', '5','6','7, extremely trustworthy'],
    )
