from django.shortcuts import render
from .forms import PlayForm, ListForm, PlayerForm
from datetime import datetime, timedelta

from .models import Player, Play, List, Dealer

def index(request):    
    return render (request, 'web/index.html')

def lists(request):
    lists = List.objects.all()
    content = {'lists': lists}
    return render (request, 'web/lists.html', content)

def plays(request, id):
    form = PlayForm
    list = List.objects.get(id=id)
    plays = list.plays.all()
    strikeTotal = 0
    boxTotal = 0
    bolaTotal = 0
    for play in plays:
        strikeTotal = strikeTotal + play.strike
        boxTotal = boxTotal + play.box
        bolaTotal = bolaTotal + play.bola
    total = strikeTotal + boxTotal + bolaTotal
    content = {'id': id, 'list': list, 'form': form, 'plays': plays, 'strikeTotal': strikeTotal, 'boxTotal': boxTotal, 'bolaTotal': bolaTotal, 'total': total}
    if request.method == 'POST':
        formValues = form(request.POST)
        if formValues.is_valid():
            if int(request.POST["number"]) <= 999:
                player = Player.objects.get(id=request.POST["player"])
                newPlay = Play(player=player, number=request.POST["number"], strike=request.POST["strike"], box=request.POST["box"], bola=request.POST["bola"])
                newPlay.save()
                list.plays.add(newPlay)
                list.save()
                content['plays'] = list.plays.all()
                return render (request, 'web/plays.html', content)
        return render (request, 'web/plays.html', content)
    return render (request, 'web/plays.html', content)

def createList(request):    
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    listsMade = List.objects.filter(date__year=year, date__month=month, date__day=day)
    form = ListForm
    content = {'form': form}
    if request.method == 'POST':
        formValues = form(request.POST)
        if formValues.is_valid():
            if listsMade.count() < 2:
                if listsMade.count() != 0:
                    for list in listsMade:
                        if list.section == 'Day' and request.POST['section'] == 'Day':
                            message = 'Ya se creo la lista del dia'
                        elif list.section == 'Night' and request.POST['section'] == 'Night':
                            message = 'Ya se creo la lista de la noche'
                        else:
                            message = 'Lista creada'
                            formValues.save()
                else:
                    message = 'Lista creada'
                    formValues.save()
            else:
                message = 'Ya estan creadas las listas de hoy'
            lists = List.objects.all()
            content = {'lists': lists, 'message': message}
            return render (request, 'web/lists.html', content)
    return render(request, 'web/createList.html', content)

def closeList(request, id):
    list = List.objects.get(id=id)
    list.closed = True
    list.date = datetime.now()
    list.save()
    lists = List.objects.all()
    content = {'lists': lists}
    return render (request, 'web/lists.html', content)

def players(request):
    players = Player.objects.all()
    content = {'players': players}
    return render (request, 'web/players.html', content)

def createPlayer(request):
    form = PlayerForm
    content = {'form': form}
    if request.method == 'POST':        
        formValues = form(request.POST)
        if formValues.is_valid():            
            formValues.save()
            players = Player.objects.all()
            content = {'players': players}
            return render (request, 'web/players.html', content)
    return render (request, 'web/createPlayer.html', content)