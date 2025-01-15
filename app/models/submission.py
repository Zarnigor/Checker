from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DateTimeField, TextField

from app.models import Problem


class Submission(Model):
    class Result(TextChoices):
        ACCEPTED = 'AC', 'Accepted'
        WRONG_ANSWER = 'WA', 'Wrong Answer'

    submitted = DateTimeField(auto_now=True)
    user = ForeignKey(User, on_delete=CASCADE)
    problem = ForeignKey(Problem, on_delete=CASCADE)
    source_code = TextField()
    result = CharField(max_length=2, choices=Result, default=Result.WRONG_ANSWER)
