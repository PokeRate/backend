from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def comments(self):
        return self.comments_set.all()
