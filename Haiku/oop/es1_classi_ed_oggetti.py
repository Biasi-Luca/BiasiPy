class film:

   def __init__(self, titolo, genere, durata, regista, produzione):
     self.titolo = titolo
     self.genere = genere
     self.durata = durata
     self.regista = regista
     self.produzione = produzione  
   def scheda(self):
        return f'\ntitolo "{self.titolo}"\nGenere: {self.genere}\nDurata:{self.durata}\nRegista:{self.regista}\nProduzione:{self.produzione}'

bandersnatch= film("bandersnatch","fantascienza","90 minuti","David Slade","Netflix")

print(bandersnatch.scheda())