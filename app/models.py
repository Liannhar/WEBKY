from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

# Create your models here.




class TagManager(models.Manager):
 def get_all(self):
  return self.all()

 def find_by_id(self, id):
  try:
   vote = self.get(pk=id)
  except ObjectDoesNotExist:
   raise Http404
  return vote


class Tag(models.Model):
 name = models.CharField(max_length=15)
 objects = TagManager()

 def __str__(self):
  return f'Tag {self.name}'


class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 avatar = models.ImageField(blank=True, null=True, upload_to="media")


class QuestionManager(models.Manager):
 def get_hot_questions(self):
  return self.filter(status__exact='h')

 def get_new_questions(self):
  return self.order_by('-date')

 def get_tagged_questions(self, tag):
  return self.filter(tag__exact=tag)

 def get_questions(self):
  return self.all()

 def find_by_id(self, id):
  try:
   vote = self.get(pk=id)
  except ObjectDoesNotExist:
   raise Http404
  return vote


class AnswerManager(models.Manager):
 def get_answers(self, question):
  return self.filter(question__exact=question)

 def get_answers_count(self, question):
  return self.filter(question__exact=question).count()


class LikeManager(models.Manager):
 def get_answers_likes(self, answer):
  return self.filter(answer__exact=answer).count()

 def get_questions_likes(self, question):
  return self.filter(question__exact=question).count()


# q = models.Question.objects.get_tagged_questions(1)


class Question(models.Model):
 title = models.CharField(max_length=60)
 tag = models.ManyToManyField(Tag)
 text = models.TextField()
 user = models.ForeignKey(Profile, related_name='profile_related', on_delete=models.CASCADE, blank=True, null=True)

 HOT = 'h'
 NORMAL = 'n'
 STATUSES = [
  (HOT, 'hot'),
  (NORMAL, 'ok')
 ]

 status = models.CharField(max_length=1, choices=STATUSES)
 date = models.DateTimeField(blank=True, null=True)
 objects = QuestionManager()

 def __str__(self):
  return f'Question {self.title}'


class Answer(models.Model):
 text = models.TextField()
 user = models.ForeignKey(Profile, related_name='profile_related1', on_delete=models.CASCADE, blank=True, null=True)
 question = models.ForeignKey(Question, related_name='question_related', on_delete=models.CASCADE, blank=True,
                              null=True)
 objects = AnswerManager()


class LikeQuestion(models.Model):
 question = models.ForeignKey(Question, related_name="question_like", on_delete=models.CASCADE)
 profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

 def __str__(self):
  return f"{self.profile.user.username} {self.question.title}"

 objects = LikeManager()


class LikeAnswer(models.Model):
 user = models.ForeignKey(Profile, related_name='profile_related3', on_delete=models.CASCADE, blank=True, null=True)
 answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True,null=True)

 objects = LikeManager()


