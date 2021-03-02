nome= input("quale è il tuo nome?")
print(nome)
cognome= input("quale è il tuo cognome?")
nome_cognome= print(nome+" "+cognome)
print("il numero di caratteri totali è",len(str(nome))+len(str(cognome)))

numeroA=input("scrivi un numero")
numeroB=input("scrivi un altro numero")
if numeroA<numeroB:
    print("il numero più piccolo è",numeroA,", ","quello più grande invece",numeroB)
else:
    print("il numero più piccolo è",numeroB,", ","quello più grande invece", numeroA)

colore_preferito=input("quale è il tuo colore preferito")
if colore_preferito =="rosso":
    print("bello")
elif colore_preferito=="Rosso":
    print("bello")
elif colore_preferito=="ROSSO":
    print("bello")
else:
    print("non mi piace")

lista1=[nome]
for elemento in range(3):
    print(nome)


for lettera in nome:
    print(lettera)

    

frutta=('banana','ananas','mela','pera')
print(frutta[3])

scelta=input("scegli una frutta tra bannana, ananas, mela e pera ")
if scelta.lower == "banana":
    print(frutta.index('banana'))
elif scelta.lower == "mela":
    print(frutta.index('mela'))
elif scelta.lower == 'ananas':
    print(frutta.index('ananas'))
elif scelta.lower == 'pera':
    print(frutta.index('pera'))



lista2=["a","b","c","d","e"]
for lettera in range(1):
    print(lista2)

lista3=["23","83","552","0","92","73","10","17","44","25"]
lista3.sort()
print(lista3)
