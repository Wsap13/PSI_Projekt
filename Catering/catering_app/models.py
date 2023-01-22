from django.db import models


class Pracownicy(models.Model):
    imie = models.CharField(null= False,max_length=45)
    nazwisko = models.CharField(null= False,max_length=45)
    KUCHARZ='kuc'
    KIEROWCA='kier'
    POMOCNIK='pom'
    STANOWISKO_CHOICES=((KUCHARZ,'kucharz'),(KIEROWCA,'kierowca'),(POMOCNIK,'pomocnik'))
    stanowisko = models.CharField(max_length=5, choices=STANOWISKO_CHOICES, default=KIEROWCA)
    pensja = models.DecimalField(null= False,max_digits=14, decimal_places=2)  
    pesel = models.CharField(null= False,max_length=11)

    class Meta:
        ordering = ('imie',)

    def __str__(self):
        return self.imie+" "+self.nazwisko

class Magazyn(models.Model):
    towary = models.CharField(null= False,max_length=45)
    ilosc = models.IntegerField(null= False)
    data_przydatnosci = models.DateTimeField(null= False,auto_now=False, auto_now_add=False)

class Posilki(models.Model):
    posilek_nazwa = models.CharField(null= False,max_length=50)
    cena = models.FloatField(null= False)
    NORMALNY='norm'
    WEGANSKI='wega'
    WEGETARIANSKI='wege'
    TYP_CHOICES=((NORMALNY,'normalny'),(WEGANSKI,'wegański'),(WEGETARIANSKI,'wegetariański'))
    typ = models.CharField(max_length=5, choices=TYP_CHOICES, default=NORMALNY)

class Klient(models.Model):
    imie_klienta = models.CharField(null= False,max_length=100,default='')
    nazwisko_klienta = models.CharField(null= False,max_length=100,default='')
    adres_klienta = models.CharField(null= False,max_length=50)
  
    class Meta:
        ordering = ('imie_klienta',)

    def __str__(self):
        return self.imie_klienta+" "+self.nazwisko_klienta


class Zamowienia(models.Model):
    suma = models.DecimalField(null= False,max_digits=14, decimal_places=2)
    posilki= models.ForeignKey(Posilki, on_delete=models.CASCADE)
    data = models.DateField()
    dane_klienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
# Create your models here.