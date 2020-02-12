from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from streams.forms import DropDown

def choice(request):
    if request.method == 'POST':
        form = DropDown(request.POST)
        if form.is_valid():
            chosen_stream = form.cleaned_data['chosen_stream']
            return HttpResponseRedirect(reverse('streams:stream', args=[chosen_stream]))
    else:
        form = DropDown()
    return render(request, 'streams/choices.html', {'form': form})

def stream(request, chosen_stream):
    if (chosen_stream == 'hermon'):
        stream_name = 'https://g0.ipcamlive.com/player/player.php?alias=5a2d812803c36'
    elif (chosen_stream == 'bansko'):
        stream_name = 'https://livestream.com/accounts/89344/events/8528180/player?width=960&height=540&enableInfoAndActivity=false&defaultDrawer=&autoPlay=true&mute=false'
    return render(request, 'streams/streams.html', {'stream_name': stream_name})
