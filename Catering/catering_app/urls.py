from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('pracownicy', views.PracownicyList.as_view(), name=views.PracownicyList.name),
    path('pracownicy/<int:pk>', views.PracownicyDetail.as_view(), name=views.PracownicyDetail.name),
    path('magazyn', views.MagazynList.as_view(), name=views.MagazynList.name),
    path('magazyn/<int:pk>', views.MagazynDetail.as_view(), name=views.MagazynDetail.name),
    path('posilki', views.PosilkiList.as_view(), name=views.PosilkiList.name),
    path('posilki/<int:pk>', views.PosilkiDetail.as_view(), name=views.PosilkiDetail.name),
    path('klient', views.KlientList.as_view(), name=views.KlientList.name),
    path('klient/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('zamowienia', views.ZamowieniaList.as_view(), name=views.ZamowieniaList.name),
    path('zamowienia/<int:pk>', views.ZamowieniaDetail.as_view(), name=views.ZamowieniaDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]   