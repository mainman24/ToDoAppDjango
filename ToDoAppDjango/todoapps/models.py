from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
