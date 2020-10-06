#Nomor 1
class List2D(list):
    def __add__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]+obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")
            
    def __sub__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]-obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")
    
    def __mul__(self,obj):
        if len(self[0])==len(obj):
            hsl=[]
            for x in range(len(self)):
                tmp = []
                for y in range(len(self)):
                    bil = 0
                    for z in range(len(self[0])):
                        bil += (self[x][z] * obj[z][y])
                    tmp.append(bil)
                hsl.append(tmp)
            return List2D(hsl)
    
    def determinant(self):
        if len(self[0])==2 and len(self)==2:
            det=(self[0][0]*self[1][1])-(self[0][1]*self[1][0])
            print(det) 
        else:
            print("Ukuran matriks harus 2x2")
            
    def __invert__(self):
        if len(self[0])==2 and len(self)==2:
            hsl=[]
            mat=[[self[1][1],-self[0][1]],[-self[1][0],self[0][0]]]
            inv=(1/((self[0][0]*self[1][1])-(self[0][1]*self[1][0])))
            for i in range(len(mat)):
                tmp=[]
                for j in range(len(mat[0])):
                    tmp.append(inv*mat[i][j])
                hsl.append(tmp)
            return List2D(hsl)
        else:
            print("Ukuran matriks harus 2x2")
            
    def __str__(self):
        for i in range(len(self)):
            print("|",end=" ")
            for j in range(len(self[0])):
                print("%.2f" % self[i][j],end=" ")
            print("|")
        return ""
class List2D(list):
    def __add__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]+obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")

    def __sub__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]-obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")

    def __mul__(self,obj):
        if len(self[0])==len(obj):
            hsl=[]
            for x in range(len(self)):
                tmp = []
                for y in range(len(self)):
                    bil = 0
                    for z in range(len(self[0])):
                        bil += (self[x][z] * obj[z][y])
                    tmp.append(bil)
                hsl.append(tmp)
            return List2D(hsl)

    def determinant(self):
        if len(self[0])==2 and len(self)==2:
            det=(self[0][0]*self[1][1])-(self[0][1]*self[1][0])
            print(det)
        else:
            print("Ukuran matriks harus 2x2")

    def __invert__(self):
        if len(self[0])==2 and len(self)==2:
            hsl=[]
            mat=[[self[1][1],-self[0][1]],[-self[1][0],self[0][0]]]
            inv=(1/((self[0][0]*self[1][1])-(self[0][1]*self[1][0])))
            for i in range(len(mat)):
                tmp=[]
                for j in range(len(mat[0])):
                    tmp.append(inv*mat[i][j])
                hsl.append(tmp)
            return List2D(hsl)
        else:
            print("Ukuran matriks harus 2x2")

    def __str__(self):
        for i in range(len(self)):
            print("|",end=" ")
            for j in range(len(self[0])):
                print("%.2f" % self[i][j],end=" ")
            print("|")
        return ""
class List2D(list):
    def __add__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]+obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")

    def __sub__(self,obj):
        if len(self[0])==len(obj[0]) and len(self) == len(obj):
            hsl=[]
            for i in range(len(self)):
                temp=[]
                for j in range(len(self[0])):
                    temp.append(self[i][j]-obj[i][j])
                hsl.append(temp)
            return List2D(hsl)
        else:
            print("Ukuran matriks tidak sama!!!")

    def __mul__(self,obj):
        if len(self[0])==len(obj):
            hsl=[]
            for x in range(len(self)):
                tmp = []
                for y in range(len(self)):
                    bil = 0
                    for z in range(len(self[0])):
                        bil += (self[x][z] * obj[z][y])
                    tmp.append(bil)
                hsl.append(tmp)
            return List2D(hsl)

    def determinant(self):
        if len(self[0])==2 and len(self)==2:
            det=(self[0][0]*self[1][1])-(self[0][1]*self[1][0])
            print(det)
        else:
            print("Ukuran matriks harus 2x2")

    def __invert__(self):
        if len(self[0])==2 and len(self)==2:
            hsl=[]
            mat=[[self[1][1],-self[0][1]],[-self[1][0],self[0][0]]]
            inv=(1/((self[0][0]*self[1][1])-(self[0][1]*self[1][0])))
            for i in range(len(mat)):
                tmp=[]
                for j in range(len(mat[0])):
                    tmp.append(inv*mat[i][j])
                hsl.append(tmp)
            return List2D(hsl)
        else:
            print("Ukuran matriks harus 2x2")

    def __str__(self):
        for i in range(len(self)):
            print("|",end=" ")
            for j in range(len(self[0])):
                print("%.2f" % self[i][j],end=" ")
            print("|")
        return ""
a = List2D([[3,4,5],[1,2,2]])
b = List2D([[2,1,1],[1,0,5]])
c = List2D([[1,1],[2,2],[3,3]])
jumlah = a+b
kali = a*c
print(a)
print(b)
print(jumlah)
print(c)
print(kali)
d = List2D([[1,2],[3,4]])
print(d)
d.determinant()
d1 = d
print(d1)
hasil = d*d1
print(hasil)


#n0m0r 2
class Dictionary(dict):
    def concat(self,obj):
        c=self.copy()
        for i in self.keys() and obj.keys():
            c[i]=obj[i]
        return Dictionary(c)
    
    def __add__(self,obj):
        c=self.copy()
        for i in self.keys():
            for j in obj.keys():
                if i==j:
                    c[i]=self[i]+obj[i]
                else:
                    c[j]=obj[j]
        return Dictionary(c)
    
    def __sub__(self,obj):
        c=self.copy()
        for i in self.keys():
            for j in obj.keys():
                if i==j:
                    c[i]=self[i]-obj[i]
                else:
                    c[j]=obj[j]
        return Dictionary(c)
    
    def exp(self,n):
        c=self.copy()
        for i in self.keys():
            c[i]=self[i]**n
        return Dictionary(c)
    
    def sort(self):
        ind=list(self)
        hsl={}
        for i in range(len(ind)-1,-1,-1):
            for j in range(i):
                if self[ind[j]]>self[ind[j+1]]:
                    temp=ind[j]
                    ind[j]=ind[j+1]
                    ind[j+1]=temp
        for x in ind:
            hsl[x]=self[x]
        return Dictionary(hsl)
a = Dictionary({1:10,2:20,3:30})
b = Dictionary({3:30,5:50,3:90})

print('A=' ,a.keys(),a . values())

concatDictionary = a.concat(b)
print('a=' ,a)
print('b=' ,b)
print('concatDictionary=' ,concatDictionary)

sumDictionary = a+b
print('a=' ,a)
print('b=' ,b)
print('sumDictionary=' ,sumDictionary)

subDictionary=a-b
print('a=' ,a)
print('b=' ,b)
print('subDictionary=' ,subDictionary)

exDictionary=a.exp(2)
print('a=' ,a)
print('exDictionary=' ,exDictionary)
b = Dictionary({3:30,1:50,2:20,9:2})

sortData = b.sort()
print('data= ', b)
print('data urut =', sortData)
