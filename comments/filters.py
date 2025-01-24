import django_filters

from .models import Comments


class CommentsFilter(django_filters.FilterSet):
    class Meta:
        model = Comments
        fields = {
            'pokemon': ['exact'],
            'user': ['exact'],
        }
