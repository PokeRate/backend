from django.db import models

from common.models import TimeStampedModel


class Comments(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    pokemon = models.ForeignKey('pokemon.Pokemon', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment
