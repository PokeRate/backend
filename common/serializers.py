from rest_framework import serializers


class TimeStampedModelSerializer(serializers.ModelSerializer):
    """Abstract model serializer with created and modified, write_only fields."""

    created = serializers.DateTimeField(write_only=True, required=False)
    modified = serializers.DateTimeField(write_only=True, required=False)

    class Meta:
        abstract = True
