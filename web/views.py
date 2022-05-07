from django.shortcuts import render
from .forms import PlayForm
from datetime import datetime
from django.utils import timezone

from .models import Player, Play

def index(request):
    return render (request, 'web/index.html')

def plays(request):
    form = PlayForm
    today = datetime.now()
    plays = Play.objects.all()
    strikeTotal = 0
    boxTotal = 0
    bolaTotal = 0
    for play in plays:
        if play.date < today:
            print('es menor', play.date, today)
        strikeTotal = strikeTotal + play.strike
        boxTotal = boxTotal + play.box
        bolaTotal = bolaTotal + play.bola
    total = strikeTotal + boxTotal + bolaTotal
    content = {'form': form, 'plays': plays, 'strikeTotal': strikeTotal, 'boxTotal': boxTotal, 'bolaTotal': bolaTotal, 'total': total}
    if request.method == 'POST':
        formValues = form(request.POST)
        if formValues.is_valid():
            if int(request.POST["number"]) > 999:
                print("error")
            formValues.save()
            return render (request, 'web/plays.html', content)
        return render (request, 'web/plays.html', content)
    return render (request, 'web/plays.html', content)

def players(request):
    players = Player.objects.all()
    content = {'players': players}
    return render (request, 'web/players.html', content)

def createPlayer(request):
    return render (request, 'web/createPlayer.html')