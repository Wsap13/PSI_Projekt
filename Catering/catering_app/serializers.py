from rest_framework import serializers
from .models import *
import datetime
from rest_framework import permissions

class PracownicySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        stanowisko = serializers.ChoiceField(choices=Pracownicy.STANOWISKO_CHOICES)
        model = Pracownicy
        fields = ['id','url','imie', 'nazwisko', 'stanowisko', 'pensja', 'pesel']
    
    def validate_pensja(self, value):
        if value <= 0:
            raise serializers.ValidationError("Pensja musi być większa od zera", )
        return value

    # def validate_imie(self, value):
    #     if value[0] in string.ascii_lowercase:
    #         raise serializers.ValidationError(
    #             "Imiona zaczynają się z dużej litery"
    #         )
    #     else:
    #         return value

    # def validate_nazwisko(self, value):
    #     if value[0] in string.ascii_lowercase:
    #         raise serializers.ValidationError(
    #             "Nazwiska zaczynają się z dużej litery"
    #         )
    #     else:
    #         return value

    # def validate_pensja(self, value):
    #     if value.any() <= 0:
    #         raise serializers.ValidationError(
    #             "Pensja nie może być mniejsza równa zero"
    #         )
    #     else:
    #         return value

class MagazynSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Magazyn
            fields = ['towary','url', 'ilosc','data_przydatnosci']

    def validate_ilosc(self, value):
        if value < 0:
            raise serializers.ValidationError("Ilosc nie moze byc mniejsza od zera", )
        return value

class PosilkiSerializer(serializers.HyperlinkedModelSerializer):
    typ = serializers.ChoiceField(choices=Posilki.TYP_CHOICES)

    class Meta:
            model = Posilki
            fields = ['posilek_nazwa','url', 'cena','typ']

    def validate_cena(self, value):
        if value <= 0:
            raise serializers.ValidationError("Cena musi być większa od zera", )
        return value

class KlientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
            model = Klient
            fields = ['id','imie_klienta', 'nazwisko_klienta','adres_klienta']

class ZamowieniaSerializer(serializers.HyperlinkedModelSerializer):
    dane_klienta = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='id')
    posilki = serializers.SlugRelatedField(queryset=Posilki.objects.all(), slug_field='posilek_nazwa')
    class Meta:
            model = Zamowienia
            fields = ['id','suma','posilki' ,'data','dane_klienta']
