from django.db import models
from datetime import datetime


class Todo(models.Model):
    due_date = models.DateTimeField('Due Date', default=datetime.now())
    title = models.CharField('Title', max_length=250)
    text = models.TextField('Text')
    complete = models.BooleanField('Completed', default=False)

    def __str__(self):
        return self.title
