from django.db import models

from common.models import TimeStampedModel


class Comments(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    pokemon = models.ForeignKey('pokemon.Pokemon', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(
        'users.User', related_name='user_likes', blank=True)

    class Meta:
        ordering = ['-created']

    @property
    def likes(self):
        return self.user_likes.count()

    def __str__(self):
        return self.comment
