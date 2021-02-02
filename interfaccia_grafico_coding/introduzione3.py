#Lavoro di Roberto Ferrigno e Luca Biasi
from guizero import *
import matplotlib.pyplot as plt


def grafico():
    f = open(paramA.value, 'r')

    coordX = []
    coordY = []


    for riga in f:
        valori = str(riga)  
        Nval = len(valori)         
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)     
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1]))
    f.close()  
    coordX.sort()
    coordY.sort()
    plt.scatter(coordX,coordY)
    plt.ylabel('alcuni numeri')
    plt.xlabel('alcuni numeri')
    plt.show()
 


app = App(title="INTERFACCIA GRAFICA",width=600, height=400 )
etichettaA = Text(app, text="scrivi il nome del file da leggere")
paramA = TextBox(app, width=30)

pushA = PushButton(app, text="Genera grafico",command=grafico, width=60, height=5)
app.display()
