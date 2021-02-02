from guizero import *
import matplotlib.pyplot as plt
def get_file():
   open("dati.txt", "r")
   
    

def grafico():
    f = open("dati.txt", 'r')

    coordX = []
    coordY = []

    
   

    for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

    f.close()  

    print ("X: ",coordX)
    print ("Y: ",coordY)

    
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

   
    print(type(coordX))
    print(type(coordY))

   

    plt.scatter(coordX,coordY)
    plt.ylabel('grafico dati')
    plt.show()
app = App(title="INTERFACCIA GRAFICA")
output = TextBox(app, width=80, height=10, multiline=True)
etichettaA = Text(app, text="scrivi dati.txt")
paramA = TextBox(app)

PushButton(app, command=get_file, text="apri file")
file_name = Text(app)
pushA = PushButton(app, text="Genera grafico",command=grafico)
app.display()
