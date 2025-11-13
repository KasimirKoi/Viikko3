"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

from datetime import datetime
#Määritellään funktiot, jotka hakevat varauksen eri tiedot
def hae_varausnumero(varaus):
    print("Varausnumero: " + varaus[0])

def hae_varaaja(varaus):
    print("Varaaja: " + varaus[1])

def hae_paiva(varaus):
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").strftime("%d.%m.%Y")
    print("Päivämäärä: " + paiva)

def hae_aloitusaika(varaus):
    print("Aloitusaika: " + varaus[3])

def hae_tuntimaara(varaus):
    print("Tuntimäärä: " + varaus[4])

def hae_tuntihinta(varaus):
    print("Tuntihinta: " + varaus[5] + " €")

def laske_kokonaishinta(varaus):
    tuntimaara = float(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimaara * tuntihinta
    print("Kokonaishinta: " + str(kokonaishinta) + " €")

def hae_maksettu(varaus):
    maksettu = "Kyllä" if varaus[6] == "True" else "Ei"
    print("Maksettu: " + maksettu)

def hae_kohde(varaus):
    print("Kohde: " + varaus[7])

def hae_puhelin(varaus):
    print("Puhelin: " + varaus[8])

def hae_sahkoposti(varaus):
    print("Sähköposti: " + varaus[9])



#Pääohjelma ja tiedoston lukeminen sekä käsittely
def main():
    varaukset = "varaukset.txt"
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

# kutsutaan funktioita
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

if __name__ == "__main__":
    main()
