

class parabola:

    

    def __init__(self,a,b,c):
        self.__a=int(a)
        self.__b=int(b)
        self.__c=int(c)
        self.punti=[]

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def fuoco(self,asse_simmetria= "x"):
        if(asse_simmetria=="x"):
            y =-((self.__b)/((self.__a)*2))
            x = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a 
            print("Le coordinate del fuoco sono ",x,y)
        elif(asse_simmetria=="y"):
           x =-((self.__b)/((self.__a)*2))
           y = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
        print("Le coordinate del fuoco sono ",x,y)

    def direttrice(self,asse_simmetria="x"):
         if (asse_simmetria == "x"):
            y= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            print("L'equazione dell'ascissa è",y) 

         elif (asse_simmetria == "y"):
            x= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            print("L'equazione dell'ascissa è",x) 

      

    

    




p = parabola(input('valore a='),input('valore b='),input('valore c='))
print(p.fuoco(input('Asse di simmetria parallelo a quale asse?')))
print(p.direttrice(input('Asse di simmetria parallelo a quale asse?')))