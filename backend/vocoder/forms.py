from django import forms 
from .models import *

class AudioForm(forms.ModelForm):
    class Meta:
        model=Vocoder_audio_carrier
        fields=['record']