from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

class PracownicyList(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'pracownicy-list'
    search_fields = ['imie', 'nazwisko','stanowisko']
    ordering_fields = ['pensja']
    permission_classes = [IsAuthenticated]

class PracownicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'pracownicy-detail'
    permission_classes = [IsAuthenticated]

class MagazynList(generics.ListCreateAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer
    search_fields = ['towary']
    ordering_fields = ['ilosc','data_przydatnosci']
    name = 'magazyn-list'
    permission_classes = [IsAuthenticated]

class MagazynDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer
    name = 'magazyn-detail'
    permission_classes = [IsAuthenticated]    

class PosilkiList(generics.ListCreateAPIView):
    queryset = Posilki.objects.all()
    serializer_class = PosilkiSerializer
    search_fields = ['posilek_nazwa','typ']
    ordering_fields = ['cena']
    name = 'posilki-list'
    permission_classes = [IsAuthenticated]
       
class PosilkiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posilki.objects.all()
    serializer_class = PosilkiSerializer
    name = 'posilki-detail'
    permission_classes = [IsAuthenticated]

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    search_fields = ['adres_klienta']
    ordering_fields = ['imie_klienta','nazwisko_klienta']
    name = 'Klient-list'
    permission_classes = [IsAuthenticated]

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-detail'
    permission_classes = [IsAuthenticated]

class ZamowieniaList(generics.ListCreateAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'Zamowienia-list'
    permission_classes = [IsAuthenticated]

class ZamowieniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'Zamowienia-detail'
    permission_classes = [IsAuthenticated]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'Lista pracowników:': reverse(PracownicyList.name, request=request),
                         'Stan magazynu: ': reverse(MagazynList.name, request=request),
                         'Lista posiłków: ': reverse(PosilkiList.name, request=request),
                         'Lista Klientów: ': reverse(KlientList.name, request=request),
                         'Lista zamówień: ': reverse(ZamowieniaList.name, request=request)
})
# class PracownicyApiView(APIView):
#     def get(self,request):
#         allPracownicy=Pracownicy.objects.all().values()
#         return Response({"Message":"Lista pracowników","Pracownicy lsita":allPracownicy})
    
#     def post(self,request):
#         Pracownicy.objects.create(imie=request.data["imie"],
#                                 nazwisko=request.data["nazwisko"],
#                                 stanowisko=request.data["stanowisko"],
#                                 pensja=request.data["pensja"],
#                                 pesel=request.data["pesel"]
#                                 )
#         pracownik=Pracownicy.objects.all().filter(id=request.data["imie"]).values()
#         return Response({"Message":"Pracownik dodany","Pracownik":pracownik})

# class PracownicyList(generics.ListCreateAPIView):
#     queryset = pracownicy.objects.all()
#     serializer_class = pracownicySerializer
#     name = 'pracownicy-list'



# Create your views here.
