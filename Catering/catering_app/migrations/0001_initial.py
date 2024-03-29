# Generated by Django 4.1.3 on 2023-01-21 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie_klienta', models.CharField(default='', max_length=100)),
                ('nazwisko_klienta', models.CharField(default='', max_length=100)),
                ('adres_klienta', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('imie_klienta',),
            },
        ),
        migrations.CreateModel(
            name='Magazyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towary', models.CharField(max_length=45)),
                ('ilosc', models.IntegerField()),
                ('data_przydatnosci', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Posilki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posilek_nazwa', models.CharField(max_length=50)),
                ('cena', models.FloatField()),
                ('typ', models.CharField(choices=[('norm', 'normalny'), ('wega', 'wegański'), ('wege', 'wegetariański')], default='norm', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('stanowisko', models.CharField(choices=[('kuc', 'kucharz'), ('kier', 'kierowca'), ('pom', 'pomocnik')], default='kier', max_length=5)),
                ('pensja', models.DecimalField(decimal_places=2, max_digits=14)),
                ('pesel', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ('imie',),
            },
        ),
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suma', models.DecimalField(decimal_places=2, max_digits=14)),
                ('data', models.DateField()),
                ('dane_klienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.klient')),
                ('posilki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.posilki')),
            ],
        ),
    ]
