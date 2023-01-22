from django.db import models

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
    dane_klienta = models.ManyToManyField(Klient)
# Create your models here.