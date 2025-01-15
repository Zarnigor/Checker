from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, TextField, BooleanField


class Problem(Model):
    class Difficulty(TextChoices):
        HARD = 'HR', 'Hard'
        MEDIUM = 'MR', 'Medium'
        EASY = 'EA', 'Easy'

    title = CharField(max_length=255)
    body = TextField()
    author = ForeignKey(User, on_delete=CASCADE)
    difficulty = CharField(max_length=2, choices=Difficulty, default=Difficulty.EASY)
    is_private = BooleanField(default=False)

    def __str__(self):
        return self.title