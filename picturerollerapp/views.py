from otree.api import Currency as c, currency_range
from . import models
from .models import Constants
from ._builtin import Page, WaitPage
import json



class Photo_rate1(Page):

    form_model = models.Player
    form_fields = ['happy','angry','surprised','fearful','sad','neutral']

    def vars_for_template(self):
        return {
            'cur_photo': 'picturerollerapp/photos/{}'.format(json.loads(self.player.photos)[self.round_number-1]),
    }

    def before_next_page(self):
        self.player.current_pic = json.loads(self.player.photos)[self.round_number-1]


class Photo_rate2(Page):

    form_model = models.Player
    form_fields = ['looks','trustworthiness']

    def vars_for_template(self):
        return {
            'cur_photo': 'picturerollerapp/photos/{}'.format(json.loads(self.player.photos)[self.round_number-1]),
    }



class Transition(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Photo_rate1,
    Photo_rate2,
    Transition,
]
