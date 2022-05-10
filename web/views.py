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
    list.collectPick3Strike = strikeTotal
    list.collectPick3Box = boxTotal
    list.collectPick3Bola = bolaTotal
    list.collectPick3Total = total
    list.save()
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
    if list.closed and list.pick3 != None:
        list.rewardPick3Strike = 0
        list.rewardPick3Box = 0
        list.rewardPick3Bola = 0
        list.rewardPick3Total = 0
        for play in plays:
            play.pick3 = list.pick3
            if list.pick3 == play.number:
                play.rewardPick3Strike = play.strike * 600
                list.rewardPick3Strike = list.rewardPick3Strike + play.rewardPick3Strike
            boxNumber = str(play.number)
            unit = boxNumber[-1] 
            if len(boxNumber) > 1:
                ten = boxNumber[-2]
            else:
                ten = '0'
            if len(boxNumber) > 2:
                hundred = boxNumber[-3]
            else:
                hundred = '0'
            if unit in str(list.pick3) and ten in str(list.pick3) and hundred in str(list.pick3):
                if ten != '0' and hundred != '0':
                    if ten == hundred or ten == unit or unit == hundred:
                        play.rewardPick3Box = play.box * 200
                    else:
                        play.rewardPick3Box = play.box * 100
                list.rewardPick3Box = list.rewardPick3Box + play.rewardPick3Box           
            pick3String = str(list.pick3 )
            decenas = int(pick3String[-2:])
            playString = str(play.number)
            decenasPlay = int(playString[-2:])
            if decenas == decenasPlay:
                play.rewardPick3Bola = play.bola * 70
                list.rewardPick3Bola = list.rewardPick3Bola + play.rewardPick3Bola
            play.save()
            list.rewardPick3Total = list.rewardPick3Strike + list.rewardPick3Box + list.rewardPick3Bola
            list.save()
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

def playerDetail(request, id):
    player = Player.objects.get(id=id)
    plays = Play.objects.filter(player=player)
    content = {'player': player, 'plays': plays}
    return render (request, 'web/playerDetail.html', content)


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