from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_movies')
    timestamp = models.DateTimeField()
    n_likes = models.PositiveIntegerField()
    n_hates = models.PositiveIntegerField()

    def __str__(self):
        return 'title:{}, user:{}, timestamp:{}'.format(self.name, self.user.username, self.timestamp)

    class Meta:
        ordering = ['timestamp']
