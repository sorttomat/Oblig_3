"""
Program som utforsker muligheter med lister.
"""

liste = [1, 2, 3]
liste.append(4)
print(liste[0], liste[2])

navn = []
for i in range(4): #Denne forlokken kjorer 4 ganger, og hver gang legges det til et navn i listen "navn".
    navn.append(input("Skriv inn et navn: "))

if "Christine" in navn or "christine" in navn: #Ettersom baade store og smaa bokstaver kan forekomme, tok jeg hoyde for det.
    print("Du husket meg!")
else:
    print("Glemte du meg?")

nyListe = liste + navn
print(nyListe)
del nyListe[-2:]
print(nyListe)
