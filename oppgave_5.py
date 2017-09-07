# Krigsskip

from random import randint


def printBrett(brett):
    for rad in brett:
        print(" ".join(rad))


def krigsskipRad(brett):
    return randint(0, len(brett) - 1)

def krigsskipKolonne(brett):
    return randint(0, len(brett) - 1)

def gjettRad(brett):
    gjettetRad = int(input("Gjett hvilken rad skipet befinner seg paa: "))
    while gjettetRad >= len(brett):
        gjettetRad = int(input("Saa mange rader finnes ikke, gjett paa et tall mellom 0 og {}: ".format(len(brett)- 1)))
    return gjettetRad

def gjettKolonne(brett):
    gjettetKolonne = int(input("Gjett hvilken kolonne skipet ligger paa: "))
    while gjettetKolonne >= len(brett):
        gjettetKolonne = int(input("Saa mange kolonner finnes ikke, gjett paa et tall mellom 0 og {}: ".format(len(brett)- 1)))
    return gjettetKolonne

def xMarksTheSpot(brett, gjettetRad, gjettetKolonne):
    brett[gjettetRad][gjettetKolonne] = "X"
    return brett


def krigsskipSpill():
    brett = [["O"] *5 for i in range(5)]
    rad = krigsskipRad(brett)
    kolonne = krigsskipKolonne(brett)

    print("Klarer du aa senke krigsskipet mitt? Du faar bare tre forsok!")

    for i in range(3):
        printBrett(brett)
        gjettetRad = gjettRad(brett)
        gjettetKolonne = gjettKolonne(brett)

        if gjettetRad == rad and gjettetKolonne == kolonne:
            print("Gratulerer! Du sank skipet mitt!")
            break
        else:
            if i == 2:
                print("Du klarte ikke aa senke skipet mitt, din landkrabbe!")
            else:
                forsokIgjen = 2 - i
                print("Du bommet! Naa har du bare {} forsok igjen.".format(forsokIgjen))
            brett[gjettetRad][gjettetKolonne] = "X"
        
    

krigsskipSpill()







