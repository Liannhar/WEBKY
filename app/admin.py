from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Question, Answer, Tag, Profile, \
    LikeQuestion, LikeAnswer

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(LikeQuestion)
admin.site.register(LikeAnswer)