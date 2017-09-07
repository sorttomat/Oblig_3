"""
Dette programmet oppretter en dictionary, legger inn to nye keys med tilhorende 
values og printer ut dictionaryen.
"""

butikk = {
"melk" : 14.9,
"brod" : 24.9,
"yoghurt" : 12.9,
"pizza" : 39.9
}

print(butikk)

for i in range(2):
    produkt = input("Skriv inn et produkt: ")
    pris = input("Skriv inn prisen paa produktet: ")
    butikk[produkt] = pris

print(butikk)
