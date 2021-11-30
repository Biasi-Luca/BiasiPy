# La classe retta
import math
class retta:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):

    # un attributo privato si dichiara con il doppio underscore ( __ )    
      if(tipo == "param"):
         self.__a = int(p1)  
         self.__b = int(p2)
         self.__c = int(p3)
         self.__punti= []
      elif(tipo == "punti"):
            self.__punti=[]
            self.__x1 = int(p1)
            self.__x2 = int(p2)
            self.__y1 = int(p3)
            self.__y2 = int(p4)
            x_d = (self.__x2 - self.__x1)
            y_d = (self.__y2 - self.__y1)
            MCD = math.gcd(x_d, y_d)
            mcm = (x_d * y_d) / MCD
            self.__a = mcm / x_d
            self.__b = mcm / y_d
            self.__c = (mcm / x_d * -self.__x2) + (mcm / y_d * self.__y2)
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)

      elif(tipo == "coeff"):
            self.__punti= []
            self.__x3 = int(p1)
            self.__y3 = int(p2)
            self.__m1 = int(p3)
            self.__a = self.__m1
            self.__b = -1
            self.__c = (self.__m1 * -self.__x3)+self.__y3
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)  
  
    def getA(self):
        return self.__a
    
    def getB(self):
        return  self.__b

    def getC(self):
        return self.__c

    def instersezione(self, a1 , b1 , c1):
        self.__a1 = float(a1)
        self.__b1 = float(b1)
        self.__c1 = float(c1)
        if (-self.__b / self.__a) == (-self.__b1 / self.__a1):
            if self.__c == self.__c1:
                return self.__punti
            else:
                return None
        elif self.__c == self.__c1:
            return (0,self.__c)
        else:
            return ((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1)), ((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))

    def equazione_imp(self):
        
        if(self.__b>0 and self.__c>0):
            return f'{str(self.__a)}x +{str(self.__b)}y +{str(self.__c)} = 0'    
        elif(self.__b<0 and self.__c>0):
            return f'{str(self.__a)}x {str(self.__b)}y + {str(self.__c)} = 0'
        elif(self.__b>0 and self.__c<0):
            return f'{str(self.__a)}x + {str(self.__b)}y {str(self.__c)} = 0'
        else:
            return f'{str(self.__a)}x {str(self.__b)}y {str(self.__c)} = 0'

    def equazione_esp(self):
        if(self.__a>0 and self.__b>0 and self.__c>0) :
            return f'y = (-{str(self.__a)}x -{str(self.__c)})/{str(self.__b)}'
        elif(self.__a<0 and self.__b>0 and self.__c>0):
            return f'y = ({str(abs(self.__a))}x -{str(self.__c)})/{str(self.__b)}'
        elif(self.__a<0 and self.__b<0 and self.__c>0):
            return f'y = ({str(abs(self.__a))}x -{str(self.__c)})/{str(self.__b)}'
        elif(self.__a<0 and self.__b<0 and self.__c<0):
            return f'y = ({str(abs(self.__a))}x +{str(abs(self.__c))})/{str(self.__b)}'
        elif(self.__a>0 and self.__b<0 and self.__c<0):
            return f'y = (-{str(self.__a)}x +{str(abs(self.__c))})/{str(self.__b)}' 
        elif(self.__a>0 and self.__b>0 and self.__c<0):
            return f'y = (-{str(self.__a)}x +{str(abs(self.__c))})/{str(self.__b)}' 
        elif(self.__a<0 and self.__b>0 and self.__c<0):
            return f'y = ({str(abs(self.__a))}x +{str(abs(self.__c))})/{str(self.__b)}'
        elif(self.__a>0 and self.__b<0 and self.__c<0):
             return f'y = (-{str(self.__a)}x +{str(abs(self.__c))})/{str(self.__b)}' 
        elif(self.__a>0 and self.__b<0 and self.__c>0):  
            return f'y = (-{self.__a}x -{self.__c})/{self.__b}'    
    #8 e 5 uguali




    def trova_y(self, x):
       self.__x = float(x) 
       return f" y = {(-self.__a / self.__b)* self.__x + (-self.__c / self.__b)}"



    def m(self):
      if self.__b == 0:
       return None
      else:
       return -((self.__a))/((self.__b))


    def punti(self, k, h):
        self.k = int(k)
        self.h = int(h)
    
        for self.k in range (self.h):
            tupla = (self.__x, (-self.__a * self.__x) / self.__b + (-self.__c / self.__b))
            self.__x = self.__x + 1
            self.__punti.append(tupla)
        return self.__punti


      
   















         

        












        

    


# inizio del programma chiamante


r = retta(input('tipo='),input('valore 1='),input('valore 2='),input('valore 3='),input('valore 4='))

print("l'equazione implicita è",r.equazione_imp())
print("l'equazione esplicita è",r.equazione_esp())
print("Il coefficiente angolare è",r.m())
print(r.trova_y(input('x =')))
print(r.instersezione(input('a1 = ' ), input('b1 = ' ), input('c1 = ' )))
print("Le coordinate dei punti appartenenti alla retta sono:",(r.punti(input('inizio intervallo = ') , input('fine intervallo = '))))
