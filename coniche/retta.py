# La classe retta

class retta:
    def __init__(self,a,b,c):

    # un attributo privato si dichiara con il doppio underscore ( __ )    
        self.__a = a  
        self.__b = b
        self.__c = c

    def equazione_imp(self):
        if(self.__b>0 and self.__c>0):
            return f'{self.__a}x + {self.__b}y + {self.__c} = 0'
        elif(self.__b<0 and self.__c>0):
            return f'{self.__a}x {self.__b}y + {self.__c} = 0'
        elif(self.__b>0 and self.__c<0):
            return f'{self.__a}x + {self.__b}y {self.__c} = 0'
        else:
            return f'{self.__a}x {self.__b}y {self.__c} = 0'

    def equazione_esp(self):
        if(self.__a>0 and self.__b>0 and self.__c>0) :
            return f'y = (-{self.__a}x -{self.__c})/{self.__b}'
        elif(self.__a<0 and self.__b>0 and self.__c>0):
            return f'y = ({abs(self.__a)}x -{self.__c})/{self.__b}'
        elif(self.__a<0 and self.__b<0 and self.__c>0):
            return f'y = ({abs(self.__a)}x -{self.__c})/{self.__b}'
        elif(self.__a<0 and self.__b<0 and self.__c<0):
            return f'y = ({abs(self.__a)}x +{abs(self.__c)})/{self.__b}'
        elif(self.__a>0 and self.__b<0 and self.__c<0):
            return f'y = (-{self.__a}x +{abs(self.__c)})/{self.__b}' 
        elif(self.__a>0 and self.__b>0 and self.__c<0):
            return f'y = (-{self.__a}x +{abs(self.__c)})/{self.__b}' 
        elif(self.__a<0 and self.__b>0 and self.__c<0):
            return f'y = ({abs(self.__a)}x +{abs(self.__c)})/{self.__b}'
        elif(self.__a>0 and self.__b<0 and self.__c<0):
             return f'y = (-{self.__a}x +{abs(self.__c)})/{self.__b}' 
        elif(self.__a>0 and self.__b<0 and self.__c>0):  
            return f'y = (-{self.__a}x -{self.__c})/{self.__b}'    












        

    


# inizio del programma chiamante


r = retta(-3,-4,-6)

print(r.equazione_imp())
print(r.equazione_esp())


# il metodo dir permette di conoscere tutti i metodi applicabili all'oggetto passato come parametro
print(dir(r))