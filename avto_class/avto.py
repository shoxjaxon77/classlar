class Avto:
    def __init__(self,nomi,rangi,korobka,narxi,yili):
        self.nomi  = nomi
        self.rangi = rangi
        self.korobka = korobka
        self.narxi = narxi
        self.yili = yili
        self.kilometr = 0
    
    # def get_info(self):
    #     return f"nomi: {self.nomi}\nrangi: {self.rangi}\nkorobka: {self.korobka}\nnarxi: {self.narxi}$\nyili: {self.yili}\n"

    def __repr__(self):
        return self.nomi

class Avtosalon:
    def __init__(self,nomi,manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtolar = []

    def get_info(self):
        return f"Nomi: {self.nomi}\nManzili: {self.manzili}\nSotuvdagi mashinalar: {self.avtolar}\n"    
        
    def __call__(self,*x):
        self.avtolar.extend(x)

    def __getitem__(self,x):
        return self.avtolar[x-1]
    
    def __setitem__(self,x,n):
        self.avtolar[x-1] = n


    


    

