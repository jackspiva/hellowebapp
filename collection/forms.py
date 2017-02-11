from django.forms import ModelForm

from collection.models import Worksheet

class WorksheetForm(ModelForm):
    class Meta:
        model = Worksheet
        fields = ('name', 'description',)
