def beregnBillettpris():
    """
    Denne funksjonen tar inn en alder fra brukeren, og beregner billettpris
    utifra denne.
    """
    alder = float(input("Skriv inn alderen din: "))
    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif 17 < alder < 63:
        billettpris = 50
    else:
        billettpris = 35

    print("Billettprisen blir:" , billettpris)

"""
Jeg ser ikke helt problemet med prosedyren. Hvis jeg hadde fulgt "oppskriften"
i oppgaveteksten naar det gjaldt if-else-sjekken, saa hadde jeg faatt et
problem med at billettprosen forst hadde blitt 50 og deretter 35 hvis alderen
var over eller lik 63. Dette fikset jeg i min kode.
"""

for i in range(4):
    beregnBillettpris()
