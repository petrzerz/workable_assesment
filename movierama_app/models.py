from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_movies')
    timestamp = models.DateTimeField(auto_now=True)
    n_likes = models.PositiveIntegerField(null=True)
    n_hates = models.PositiveIntegerField(null=True)

    def __str__(self):
        return 'title:{}, user:{}, timestamp:{}'.format(self.title, self.user.username, self.timestamp)

    def get_absolute_url(self):
        # return reverse('movie-detail', args=(str(self.id)))
        return reverse('home')

    class Meta:
        ordering = ['timestamp']
