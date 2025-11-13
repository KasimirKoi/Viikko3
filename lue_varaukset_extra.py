#Tuodaan tarvittava kirjasto päivämäärien käsittelyyn
from datetime import datetime

#Funktiot varauksen tietojen hakemiseen ja tulostamiseen
def hae_varausnumero(varaus):
    print("Varausnumero:", varaus[0])

def hae_varaaja(varaus):
    print("Varaaja:", varaus[1])

def hae_paiva(varaus):
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").strftime("%d.%m.%Y")
    print("Päivämäärä:", paiva)

def hae_aloitusaika(varaus):
    print("Aloitusaika:", varaus[3])

def hae_tuntimaara(varaus):
    print("Tuntimäärä:", varaus[4])

def hae_tuntihinta(varaus):
    print("Tuntihinta:", varaus[5], "€")

def laske_kokonaishinta(varaus):
    tuntimaara = float(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimaara * tuntihinta
    print("Kokonaishinta: " + str(kokonaishinta) + " €")

def hae_maksettu(varaus):
    maksettu = "Kyllä" if varaus[6].lower() == "true" else "Ei"
    print("Maksettu:", maksettu)

def hae_kohde(varaus):
    print("Kohde:", varaus[7])

def hae_puhelin(varaus):
    print("Puhelin:", varaus[8])

def hae_sahkoposti(varaus):
    print("Sähköposti:", varaus[9])

def tulosta_varaus(varaus):
    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
    print("-" * 30)

#Pääohjelma ja tiedoston lukeminen sekä käsittely
def main():
    tiedosto = "varaukset.txt"
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            rivit = f.readlines()
        for rivi in rivit:
            varaus = rivi.strip().split('|')
            if len(varaus) == 10:
                tulosta_varaus(varaus)
            else:
                print("Virheellinen rivi:", rivi)
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt:", tiedosto)

#Ohjelman käynnistys
if __name__ == "__main__":
    main()