

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

import random
import string
from datetime import datetime
from app import models
from app.models import Profile, Question, Answer, LikeAnswer, LikeQuestion, Tag


class Command(BaseCommand):
    def random_char(self,size):
        return ''.join(random.choice(string.ascii_letters) for x in range(size))

    def random_int(self,size):
        return (random.random() * size + 1) % size
    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('need exactly zero arguments')
        ratio:int=10000

        ratio1:int=ratio*10

        questions = models.Question.objects.all()

        questions[0].status='h'




