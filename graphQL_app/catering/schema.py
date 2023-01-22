import graphene
from graphene_django import DjangoObjectType
from .models import *

class KlientType(DjangoObjectType):
    class Meta:
        model = Klient
        fields = '__all__'

class PosilkiType(DjangoObjectType):
    class Meta:
        model = Posilki
        fields = '__all__'

class ZamowieniaType(DjangoObjectType):
    class Meta:
        model = Zamowienia
        fields = '__all__'

class Query(graphene.ObjectType):
    klient = graphene.Field(KlientType, id=graphene.ID(required=True))
    klients = graphene.List(KlientType)

    posilek = graphene.Field(PosilkiType, id=graphene.ID(required=True))
    posilki = graphene.List(PosilkiType)

    zamowienie = graphene.Field(ZamowieniaType, id=graphene.ID(required=True))
    zamowienia = graphene.List(ZamowieniaType)

    def resolve_klient(root, info, id):
        return Klient.objects.get(pk=id)

    def resolve_klients(root, info, **kwargs):
        return Klient.objects.all()

    def resolve_posilek(root, info, id):
        return Posilki.objects.get(pk=id)

    def resolve_posilki(root, info, **kwargs):
        return Posilki.objects.all()

    def resolve_zamowienie(root, info, id):
        return Zamowienia.objects.get(pk=id)

    def resolve_hotels(root, info, **kwargs):
        return Zamowienia.objects.all()

class CreateKlient(graphene.Mutation):
    class Arguments:
        imie_klienta = graphene.String(required=True)
        nazwisko_klienta = graphene.String(required=True)
        adres_klienta = graphene.String(required=True)


    klient = graphene.Field(KlientType)

    @classmethod
    def mutate(cls, root, info, imie_klienta, nazwisko_klienta, adres_klienta):
        klient = Klient()
        klient.imie_klienta = imie_klienta
        klient.nazwisko_klienta = nazwisko_klienta
        klient.adres_klienta = adres_klienta
        klient.save()
        return CreateKlient(klient=klient)


class UpdateKlient(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        imie_klienta = graphene.String(required=False)
        nazwisko_klientae = graphene.String(required=False)
        adres_klienta = graphene.String(required=False)

    klient = graphene.Field(KlientType)

    @classmethod
    def mutate(cls, root, info, id, imie_klienta=None, nazwisko_klienta=None, adres_klienta=None):
        klient = Klient.objects.filter(pk=id)
        if klient is None:
            raise Exception('Klient does not exist.')
        klient = Klient.objects.get(pk=id)
        if imie_klienta:
            klient.imie_klienta = imie_klienta
        if nazwisko_klienta:
            klient.nazwisko_klienta = nazwisko_klienta
        if adres_klienta:
            klient.adres_klienta = adres_klienta
        klient.save()
        return UpdateKlient(klient=klient)


class DeleteKlient(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            klient = Klient.objects.get(pk=id)
            klient.delete()
            success = True
        except Klient.DoesNotExist:
            success = False

        return DeleteKlient(success=success)

class CreatePosilek(graphene.Mutation):
    class Arguments:
        posilek_nazwa = graphene.String(required=True)
        cena = graphene.Float(required=True)
        typ = graphene.String(required=False, default_value="NORMALNY")

    posilek = graphene.Field(PosilkiType)

    @classmethod
    def mutate(cls, root, info, posilek_nazwa, cena, typ):
        posilek = Posilki()
        posilek.posilek_nazwa = posilek_nazwa
        posilek.cena = cena
        posilek.typ = typ
        posilek.save()

        return CreatePosilek(posilek=posilek)


class UpdatePosilek(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        posilek_nazwa = graphene.String(required=False)
        cena = graphene.Float(required=False)
        typ = graphene.String(required=False)


    posilek = graphene.Field(PosilkiType)

    @classmethod
    def mutate(cls, root, info, id, posilek_nazwa=None, cena=None, typ=None):
        posilek = Posilki.objects.filter(pk=id)
        if posilek is None:
            raise Exception('Posilek does not exist.')
        posilek = Posilki.objects.get(pk=id)
        if posilek_nazwa:
            Posilki.posilek_nazwa = posilek_nazwa
        if cena:
            Posilki.phoneNumber = cena
        if typ:
            Posilki.typ = typ
        posilek.save()
        return UpdatePosilek(posilek=posilek)


class DeletePosilek(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            posilek = Posilki.objects.get(pk=id)
            posilek.delete()
            success = True
        except posilek.DoesNotExist:
            success = False

        return DeletePosilek(success=success)


class CreateZamowienie(graphene.Mutation):
    class Arguments:
        dane_klienta = graphene.List(graphene.ID)
        posilki = graphene.ID()
        data = graphene.DateTime()
        suma = graphene.Decimal()

    zamowineie = graphene.Field(ZamowieniaType)

    @classmethod
    def mutate(cls, root, info, dane_klienta, posilki, data, suma):
        klients = Klient.objects.filter(pk__in=dane_klienta)
        zamowienie = Zamowienia.objects.create(posilki=posilki,data=data, suma=suma)

        zamowienie.dane_klienta.set(klients)
        zamowienie.save()

        return CreateZamowienie(zamowienie=zamowienie)


class UpdateZamowienie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        posilki = graphene.List(graphene.ID, required=False)
        dane_klienta = graphene.ID(required=False)
        suma = graphene.Decimal(required=False)
        data = graphene.DateTime(required=False)

    zamowienie = graphene.Field(ZamowieniaType)

    @classmethod
    def mutate(cls, root, info, id, dane_klienta=None, posilki=None, suma=None, data=None):
        zamowienia = Zamowienia.objects.filter(pk=id)
        if zamowienia is None:
            raise Exception('Trip does not exist.')
        zamowienia = Zamowienia.objects.get(pk=id)
        if zamowienia:
            klients = Zamowienia.objects.filter(pk__in=dane_klienta)
            zamowienia.dane_klienta.set(klients)
        if posilki:
            posilki = Posilki.objects.get(pk=posilki)
            zamowienia.posilki = posilki
        if suma:
            zamowienia.suma = suma
        if data:
            zamowienia.data = data
       
        zamowienia.save()
        return UpdateZamowienie(zamowienia=zamowienia)


class DeleteZamowienie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            zamowienia = Zamowienia.objects.get(pk=id)
            zamowienia.delete()
            success = True
        except zamowienia.DoesNotExist:
            success = False

        return DeleteZamowienie(success=success)



class Mutation(graphene.ObjectType):
    create_klient = CreateKlient.Field()
    update_klient = UpdateKlient.Field()
    delete_klient = DeleteKlient.Field()
    create_posilek = CreatePosilek.Field()
    update_posilek = UpdatePosilek.Field()
    delete_posilek = DeletePosilek.Field()
    create_zamowienia = CreateZamowienie.Field()
    update_zamowienia = UpdateZamowienie.Field()
    delete_zamowienia = DeleteZamowienie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


