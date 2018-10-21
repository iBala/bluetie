from django.db import models
from users.models import user
from base.models import BaseModel

# Create your models here.
class question(BaseModel):
    question_text = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=100)
    correct_answer = models.TextField()

    def __str__(self):
        return self.question_text

class exam(BaseModel):
    reattempt_allowed = models.BooleanField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    questions = models.CharField(max_length=500)

    def __str__(self):
        return self.questions

class answer(BaseModel):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer_given = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_given
