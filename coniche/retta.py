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
    #8 e 5 uguali

    def m(self)
        self.__a = abs(self.__a) 
        self.__b = abs(self.__b)
        self.__c = abs(self.__c)

        if (self.__a>0 and self.__b>0 and self.__c>0):
            return f'{self.__a} =(-{ self.__b}y-{self.__c})/x'
        elif((self.__a<0 and self.__b>0 and self.__c>0): 
            return f'{self.__a} = {self.__b}+{self.__c}/-x'
        elif(self.__a<0 and self.__b<0 and self.__c>0):   
            return f'{self.__a}=(-{self.__b}y+{self.__c})/-x'
        elif(self.__a<0 and self.__b<0 and self.__c<0):
            return f'{self.__a}=(-{self.__b}y-{self.__c})/-x'
        elif(self.__a>0 and self.__b<0 and self.__c<0):    
            return f'{self.__a} =({ self.__b}y+{self.__c})/x'
        elif(self.__a>0 and self.__b>0 and self.__c<0):
            return f'{self.__a}=(-{self.__b}y+{self.__c})/x'
        elif(self.__a<0 and self.__b>0 and self.__c<0): 
            return f'{self.__a} =({ self.__b}y-{self.__c})/-x'
        elif(self.__a>0 and self.__b<0 and self.__c>0):    
            return f'{self.__a} =({ self.__b}y-{self.__c})/x' 


        












        

    


# inizio del programma chiamante


r = retta(1,1,1)

print(r.equazione_imp())
print(r.equazione_esp())
print(r.m())


# il metodo dir permette di conoscere tutti i metodi applicabili all'oggetto passato come parametro
print(dir(r))