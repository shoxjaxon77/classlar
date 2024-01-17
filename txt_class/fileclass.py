class File:
    def __init__(self,name):
        self.name = name
        self.mas = []
        with open(f"{self.name}","w"):
            pass

    def read_text(self):
        with open(f"{self.name}" , "r") as f:
            return f.read()
    
    def write_text(self,matn):
        with open(f"{self.name}","w") as f:
            f.write(matn)

    def add_text(self,x):
        with open(f"{self.name}","a") as f:
            f.write(x)

    def first_row(self):
        with open(f"{self.name}","r") as f:
            return f.readline()

    def massiv(self):  
        a = self.read_text()
        for i in a.split('\n'):
            self.mas.append(i)
        return self.mas

    def del_abzas(self):
        with open(f"{self.name}", 'r') as f:
            a = f.read().replace('\n',' ')
        with open(f"{self.name}", 'w') as f:
            f.write(a)
    
    def __repr__(self):
        with open(f"{self.name}", 'r') as f:
            return str(len(f.read()))
    
    def __getitem__(self,x):
        return self.mas[x-1]
    
    def __setitem__(self,x,matn):
        self.mas[x-1] = matn
     
    def upper_word(self):
        a = self.read_text()
        b = ""
        for i in a.split():
            b+= i.title() + " "
        return b
    
    def upper_row(self):
        b = ""
        for i in self.mas:
            if len(i)!=0:
                b += str(i[0].title()+i[1:]) + "\n"
        self.write_text(b)
    
    def del_row(self,n):
        a = list(self.read_text().split('\n'))
        a.pop(n-1)
        b = ""
        for i in a:
            b+= str(i)+ '\n'
        self.write_text(b)

    def get_row(self,n):
        a = list(self.read_text().split('\n'))
        return a[n-1]

    def del_rows(self,n,m):
        a = list(self.read_text().split('\n'))
        r=a[:n-1]+a[m-1:]
        b = ""
        for i in r:
            b+= i + '\n'
        self.write_text(b)

    def get_rows(self,n,m):
        a = list(self.read_text().split('\n'))
        r=a[n:m+1]
        b = ""
        for i in r:
            b+= i + '\n'
        self.write_text(b)
    
    def new_file(self,n,m):
        a = list(self.read_text().split('\n'))
        r=a[n:m+1]
        b = ""
        for i in r:
            b+= i+'\n'
        with open("new_file.txt","w") as f:
            f.write(b)

    def padding_left(self,n):
        a = list(self.read_text().split('\n'))
        b = ""
        for i in a:
            b+=" "*n + i + '\n'
        self.write_text(b)

    # def append_file(self,objfile):
    #     a = self.read_text()
    #     b = objfile.read_text()
    


    

        

           

















