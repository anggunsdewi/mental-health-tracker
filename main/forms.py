from django.forms import ModelForm
from main.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["feelings", "mood_intensity"]