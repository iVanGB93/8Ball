from django import forms
from .models import Play, Player

class PlayForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.all(), label='Jugador', widget=forms.Select(attrs={
        'class': 'form-control m-1',
        'placeholder': 'Jugador'
    }))
    number = forms.IntegerField(max_value=999, label='Número', widget=forms.NumberInput(attrs={
        'class': 'form-control m-1',
        'placeholder': 'número'
    }))
    strike = forms.IntegerField(label='Strike', widget=forms.NumberInput(attrs={
        'class': 'form-control m-1',
        'placeholder': 'strike'
    }))
    box = forms.IntegerField(label='Box', widget=forms.NumberInput(attrs={
        'class': 'form-control m-1',
        'placeholder': 'box'
    }))
    bola = forms.IntegerField(label='Bola', widget=forms.NumberInput(attrs={
        'class': 'form-control m-1',
        'placeholder': 'bola'
    }))    

    class Meta:
        model = Play
        fields = ['player', 'number', 'strike', 'box', 'bola']