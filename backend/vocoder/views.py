from django.shortcuts import render
from .forms import AudioForm

# Create your views here.

def Vocoder_audio_carrier(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'aud.htm', {'form' : form}) 