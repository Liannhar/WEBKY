

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

import random
import string
from datetime import datetime
from app import models
from app.models import Profile, Question, Answer, LikeAnswer, LikeQuestion, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('need exactly zero arguments')
        ratio=10000
        for i in range(ratio):
            random_avatar = random.randint(1,4)
            user=models.User.objects.create_user(username=f"User{i}")
            profile = Profile(user=user,avatar=f"static/img/avatar-{random_avatar}")
            profile.save()
        for j in range(ratio*10):
            status=models.Question.STATUSES[j % 2]
            user=Profile.objects.get(random.randrange(ratio))
            question = Question(title=f"title{j}", text = f"text{j}", status=status, user=user)
            question.save()
        for k in range(ratio*100):
            profile=models.Profile.objects.get(random.randrange(ratio))
            question=models.Question.objects.get(random.randrange(ratio*10))
            answer = Answer(text = f"text{k}",user=profile,question=question)
            answer.save()
            for n in range(2):
                like_answer = LikeAnswer(user=profile,answer=answer)
                like_question=LikeQuestion(question=question,profile=profile)
                like_answer.save()
                like_question.save()
        for d in range(ratio):
            tag = Tag(name=f"Tag{d}")
            tag.save()


