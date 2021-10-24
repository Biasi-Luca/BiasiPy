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




    def trova_y(self, x):
       self.__x = float(x) 
       return f" y = {(-self.__a / self.__b)* self.__x + (-self.__c / self.__b)}"


#return  y =int((-((self.__a) / (self.__b))*float(x)+ self.__c)

    def m(self):
      return -((self.__a))/((self.__b))


   















         

        












        

    


# inizio del programma chiamante


r = retta(1,1,1)

print(r.equazione_imp())
print(r.equazione_esp())
print(r.m())
print(r.trova_y(input('x =')))

