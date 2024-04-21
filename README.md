# tsoha_projekti
Ajattelin aiheena liikunta sivustoa. 
Sinne pystyisi kirjautumaan käyttäjänä ja luomaan tunnukset. Sovelluksesta näkisi minkälaisia tunteja olisi tarjolla, mihin aikaan ja niiden haastavuuden. Tunteja pystyisi etsimään ja niille voisi ilmoittautua mukaan. Käyttäjä näkisi oman kalenterinsa ja pystyisi kirjaamaan itselleen erilliseen päiväkirja kohtaan muuta liikuntaansa halutessaan. Jos käyttäjä on osallistunut, jollein kurssille pystyy hän jättämään arvostelun tunnille. Näiden lisäksi käyttäjä pystyy lisäämään tunteja omiin suosikkeihinsa.

Käynnistämisohjeet:
- Kloonaa repositorio.
- Siirry kloonatun repositorion juurikansioon.
- Luo kansio .env, jonka sisälle määrittelet
  DATABASE_URL=
  SECRET_KEY=
- Aktivoi virtuaaliympäristö komennoilla 
  python3 -m venv venv
  source venv/bin/activate
- Asenna riippuvuudet komennolla 
  pip install -r ./requirements.txt
- Tietokannan saa määriteltyä komennolla 
  psql < schema.sql
- Sovellus käynnistyy komennolla 
  flask run
