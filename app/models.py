from random import randint

from django.db import models

# Create your models here.

QUESTIONS = [
    {'id': question_id,
     'answers_number':question_id*question_id,
     'text': f'Text of question #{question_id}',
     'title': f'Question #{question_id}',
     'tags': ['tag' for i in range(question_id)]
     }for question_id in range(10)
]


