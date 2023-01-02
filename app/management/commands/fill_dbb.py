

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
        for d in range(ratio):
            tag = Tag(name=f"Tag{d}")
            tag.save()
        for i in range(ratio):
            random_avatar = random.randint(1,4)
            user=models.User.objects.create_user(username=f"User{i}")
            profile = Profile(user=user,avatar=f"static/img/avatar-{random_avatar}")
            profile.save()
            for j in range(10):
                status=models.Question.STATUSES[j % 2]
                question = Question(title=f"title{j}", text = f"text{j}", status=status, user=profile)
                question.save()
                for k in range(100):
                    answer = Answer(text = f"text{k}",user=profile,question=question)
                    answer.save()
                    like_answer = LikeAnswer(user=profile,answer=answer)
                    like_question=LikeQuestion(question=question,profile=profile)
                    like_answer.save()
                    like_question.save()

