from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_movies')
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_movies')
    hates = models.ManyToManyField(User, related_name='hated_movies')

    def __str__(self):
        return 'title:{}, user:{}, timestamp:{}'.format(self.title, self.user.username, self.timestamp)

    def get_absolute_url(self):
        return reverse('home')

    def total_hates(self):
        return self.hates.count()

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['timestamp']
