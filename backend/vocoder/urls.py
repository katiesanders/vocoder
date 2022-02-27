from django.urls import path
from . import views

urlpatterns = [
    path('audio/', views.Vocoder_audio_carrier),
]