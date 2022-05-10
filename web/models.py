from django.db import models
from datetime import datetime

class Dealer(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Play(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    strike = models.PositiveIntegerField()
    box = models.PositiveIntegerField()
    bola = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.now)
    pick3 = models.IntegerField(blank=True, null=True)
    rewardPick3Strike = models.IntegerField(default=0)
    rewardPick3Box = models.IntegerField(default=0)
    rewardPick3Bola = models.IntegerField(default=0)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.player.name + " jugo " + str(self.number)

class List(models.Model):
    optionsSection = (
        ('Day', 'Day'),
        ('Night', 'Night')
    )
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    section = models.CharField(max_length=5, choices=optionsSection)
    plays = models.ManyToManyField(Play, related_name='Plays')
    date = models.DateTimeField(default=datetime.now)
    closed = models.BooleanField(default=False)
    pick3 = models.IntegerField(blank=True, null=True)
    collectPick3Strike = models.IntegerField(default=0)
    collectPick3Box = models.IntegerField(default=0)
    collectPick3Bola = models.IntegerField(default=0)
    collectPick3Total = models.IntegerField(default=0)
    rewardPick3Strike = models.IntegerField(default=0)
    rewardPick3Box = models.IntegerField(default=0)
    rewardPick3Bola = models.IntegerField(default=0)
    rewardPick3Total = models.IntegerField(default=0)

    def __str__(self):
        return self.section + " " + str(self.date)