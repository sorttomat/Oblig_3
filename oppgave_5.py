"""
Dette programmet er et spill som baserer seg loest paa spillet "Battleship".
Det gaar ut paa at et krigsskip er gjemt et sted paa spillbrettet, og saa maa
brukeren gjette hvor det befinner seg (og paa den maaten senke det).
I denne forenklede versjonen, finnes det kun ett skip paa brettet. Brukeren faar
3 forsok paa aa senke skipet.
"""

from random import randint #Jeg trenger to tilfeldige heltall, saa jeg maa importere randint.


def printBrett(brett):
    """
    Prosedyre som printer ut spillbrettet til terminalen.
    """
    for rad in brett:
        print(" ".join(rad)) #For en pen print, setter jeg sammen elementene i hver rad med et mellomrom.


def tilfeldigHeltall(lengde):
    """
    Funksjon som returnerer et tilfeldig heltall av storrelse 
    mellom 0 og en gitt lengde - 1. 
    """
    return randint(0, lengde - 1) #Maa trekke fra 1 for at tallet ikke skal kunne overskride brettets lengde.


def gjettRad(antallRader):
    """
    Funksjon som ber brukeren om aa gjette hvilken rad krigsskipet ligger paa.
    Dersom brukeren gjetter paa et tall som overskrider antall rader, 
    spor programmet om en ny gjetning.
    """
    gjettetRad = int(input("Gjett hvilken rad skipet befinner seg paa: "))
    while gjettetRad >= antallRader:
        gjettetRad = int(input("Saa mange rader finnes ikke, gjett paa et tall mellom 0 og {}: ".format(antallRader- 1)))
    return gjettetRad


def gjettKolonne(antallKolonner):
    """
    Funksjon som ber brukeren om aa gjette hvilken kolonne krigsskipet ligger paa.
    Dersom brukeren gjetter paa et tall som overskrider antall kolonner, 
    spor programmet om en ny gjetning.
    """
    gjettetKolonne = int(input("Gjett hvilken kolonne skipet ligger paa: "))
    while gjettetKolonne >= antallKolonner:
        gjettetKolonne = int(input("Saa mange kolonner finnes ikke, gjett paa et tall mellom 0 og {}: ".format(antallKolonner- 1)))
    return gjettetKolonne


def xMarksTheSpot(brett, gjettetRad, gjettetKolonne):
    """
    Funksjon som tar inn index for rad og kolonne, samt et brett (nested liste).
    Det som finnes paa den indexen blir gjort om til "X", og brettet blir returnert igjen.
    """
    brett[gjettetRad][gjettetKolonne] = "X"
    return brett


def krigsskipSpill():
    """
    Funksjonen kjorer selve spillet, og bruker da alle de ovrige funksjonene.
    """
    brett = [["O"] *5 for i in range(5)] #Oppretter en liste som bestaar av 5 nestede lister som inneholder 5 "O"'er i hver.
    antallKolonner = len(brett[0]) #Finner antall kolonner paa brettet ved aa finne lengden paa en av de nestede listene (de er saaklart like lange alle sammen).
    antallRader = len(brett)
    krigsskipRad = tilfeldigHeltall(antallRader) #Genererer en tilfeldig plassering av krigsskipet.
    krigskipKolonne = tilfeldigHeltall(antallKolonner)

    print("Klarer du aa senke krigsskipet mitt? Du faar bare tre forsok!")

    for i in range(3): #Brukeren har 3 forsok paa aa gjette riktig plassering.
        printBrett(brett)
        gjettetRad = gjettRad(antallRader)
        gjettetKolonne = gjettKolonne(antallKolonner)
        xMarksTheSpot(brett, gjettetRad, gjettetKolonne)        

        if gjettetRad == krigsskipRad and gjettetKolonne == krigskipKolonne:
            print("Gratulerer! Du sank skipet mitt!")
            break #For aa forhindre at programmet fortsetter aa kjore om brukeren gjetter riktig.
        else:
            if i == 2:
                print("Du klarte ikke aa senke skipet mitt, din landkrabbe!")
                print("Skipet laa paa rad {} kolonne {} ;)".format(krigsskipRad, krigskipKolonne))
            else:
                forsokIgjen = 2 - i
                print("Du bommet! Naa har du bare {} forsok igjen.".format(forsokIgjen))
            
    




krigsskipSpill() #Kjorer spillet







