from logging.config import stopListening

contacten = {
    "John" : "0498772810",
    "Bobby" : "0496875432",
    "Jan" : "328890267",
}
def welkom():
    print("Welkom bij de telefoonboekapp")

def vraag_naam():
    naam = input("Geef een naam of typ 'stop' om te stoppen ")

def toon_telefoon(naam):
    if naam in contacten :
        print(contacten[naam])
    else:
        print("Contact niet gevonden")

def raadpleeg_telefoonboek(contacten):
    welkom()
    vraag_naam()
    toon_telefoon(naam)
raadpleeg_telefoonboek(contacten)