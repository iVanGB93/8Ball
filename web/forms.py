from re import A
from django import forms
from .models import Play, Player, List, Dealer

class PlayerForm(forms.ModelForm):
    dealer = forms.ModelChoiceField(queryset=Dealer.objects.all(), label='dealer', widget=forms.Select(attrs={
        'class': 'form-select',
        'id': 'floatingSelect',
        'placeholder': 'Dealer'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'id': 'floatingName',
        'placeholder': 'Nombre'        
    }))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number',
        'id': 'floatingPhone',
        'placeholder': 'Teléfono',
        'value': 0       
    }))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'email',
        'id': 'floatingEmail',
        'placeholder': 'name@example.com'        
    }))
    class Meta:
        model = Player
        fields = ['dealer', 'name', 'phone', 'email']

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

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['dealer', 'section']