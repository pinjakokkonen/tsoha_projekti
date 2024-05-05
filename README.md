# tsoha_projekti
Suunnitelma:

Ajattelin aiheena liikunta sivustoa.
Sinne pystyisi kirjautumaan käyttäjänä ja luomaan tunnukset. Sovelluksesta näkisi minkälaisia tunteja olisi tarjolla, mihin aikaan ja niiden haastavuuden. Tunteja pystyisi etsimään ja niille voisi ilmoittautua mukaan. Käyttäjä näkisi oman kalenterinsa ja pystyisi kirjaamaan itselleen erilliseen päiväkirja kohtaan muuta liikuntaansa halutessaan. Jos käyttäjä on osallistunut jollein kurssille, pystyy hän jättämään arvostelun tunnille. Näiden lisäksi käyttäjä pystyy lisäämään tunteja omiin suosikkeihinsa.

Sovelluksen toiminnallisuus:
- Sovellukseen pystyy luomaan tunnukset, kirjautumaan sisään ja kirjautumaan ulos
- Käyttäjä pystyy ilmoittautumaan kursseille ja perumaan ilmoittautumisen
- Käyttäjä pystyy jättämään arvosteluita kursseille
- Käyttäjä pystyy myös kirjoittamaan itselleen omia henkilökohtaisia merkintöjä
- Kursseja pystyy hakemaan kurssin nimellä
- Admin käyttäjä pystyy lisäämään ja poistamaan kursseja

Käynnistämisohjeet:

Kloonaa repositorio.

Siirry kloonatun repositorion juurikansioon.

Luo kansio .env, jonka sisälle määrittelet
- DATABASE_URL=
- SECRET_KEY=

Aktivoi virtuaaliympäristö komennoilla 
- python3 -m venv venv
- source venv/bin/activate

Asenna riippuvuudet komennolla 
- pip install -r ./requirements.txt

Tietokannan saa määriteltyä komennolla 
- psql < schema.sql

Sovellus käynnistyy komennolla 
- flask run
