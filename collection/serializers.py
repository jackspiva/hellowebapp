from rest_framework import serializers
from collection.models import Worksheet


class WorksheetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Worksheet
        fields = ('name', 'description', 'slug',)
