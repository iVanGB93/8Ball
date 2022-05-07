from django.db import models
from datetime import datetime

class Dealer(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " de " + self.dealer.name

class Play(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    strike = models.PositiveIntegerField()
    box = models.PositiveIntegerField()
    bola = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.player.name + " jugo " + str(self.number)