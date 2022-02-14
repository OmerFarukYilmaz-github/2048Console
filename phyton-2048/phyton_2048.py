import random

# Ömer Faruk Yılmaz
# Consoleda basit 2048 oyunu 
# Adım adım ne olduğunu görmek isterseniz fonksyonlar icerisindeki yorum satırlarını yorumdan cıkarabilirsiniz.
# 26.11 



class oyun():
  
    #oyun alanı olusturulan kurucu method. 
    #Girilen matris boyutunca elemana sahip 0'lardan olusan bir liste olusturuyoruz(sutunlar) 
    #Bu diziyi oyun alanına append edip (liste içinde liste ile) matrisi (oyun alanını) olusturuyoruz. 
    def __init__(self,matrisBoyutu=4):
        self.oyunAlanı=[]
        self.matrisBoyutu=matrisBoyutu
        for i in range (matrisBoyutu):
            sutunlar=[]
            for j in range(matrisBoyutu):
                sutunlar.append(0)
            self.oyunAlanı.append(sutunlar)
        self.rastgele_DegerAta(2)
      
    # istenilen adette 2 degeri, rastgele indise/indislere atanır.
    def rastgele_DegerAta(self,n):
        i=0
        while (i<int(n)):
            i+=1
            satır = random.randint(0,self.matrisBoyutu-1)
            sutun = random.randint(0,self.matrisBoyutu-1)
            if str(self.oyunAlanı[satır][sutun]) == "0" :# o satırda baska deger varsa oraya atama yapma
                self.oyunAlanı[satır][sutun]=2
            #    print("i= ",i," [",satır,"]","[",sutun,"]"," 'a 2 degeri atandı")
            else :
                i=i-1


    #oyun alanını getiren kod
    def oyunAlanıGetir(self):
        return self.oyunAlanı

    #oyun alanını yazdıran kod
    def oyunAlanıYazdır(self):
       # maxSayı=max(self.oyunAlanı)
        maxSayı=max(self.oyunAlanı)
        for i in range(self.matrisBoyutu):
            for j in range (self.matrisBoyutu):## yazdırırken düzenli dursun diye aralıkları max sayıya göre ayarlıyoruz
                print(self.oyunAlanı[i][j],end=" ")
                #if maxSayı<10:
                #    print(self.oyunAlanı[i][j],end=" ")
                #elif maxSayı<100:
                #    print(self.oyunAlanı[i][j],end="  ")
                #if maxSayı<1000:
                #    print(self.oyunAlanı[i][j],end="   ")
            print()

    # oyunun bitip bitmediğini kontrol eden kod
    def yapılabilcek_hareket_var_mı(self):
        for i in range(self.matrisBoyutu-1):
            for j in range(self.matrisBoyutu-1):
                if(self.oyunAlanı[i][j]== self.oyunAlanı[i + 1][j] or self.oyunAlanı[i][j]== self.oyunAlanı[i][j + 1]):
                    return True
 
        for j in range(matrisBoyutu-1):
            if(self.oyunAlanı[self.matrisBoyutu-1][j]== self.oyunAlanı[self.matrisBoyutu-1][j + 1]):
                 return True
 
        for i in range(matrisBoyutu-1):
            if(self.oyunAlanı[i][self.matrisBoyutu-1]== self.oyunAlanı[i + 1][self.matrisBoyutu-1]):
                return True

        return False

    def oyunDurum(self):
        self.oyunDevam_mı=True

        for i in range (self.matrisBoyutu):
            for j in range (self.matrisBoyutu):
                if str(self.oyunAlanı[i][j])=="2048":
                    self.oyunDevam_mı=false
                    print("Tebrikler 2048 sayısını elde ettiniz!!!")
                    # Yapılcak baska hamle kaldı mı o kontrol edilecek
                    return self.oyunDevam_mı
                

        self.oyunDevam_mı=self.yapılabilcek_hareket_var_mı()
                

        if self.oyunDevam_mı==False:
            print("Kaybettiniz!")


        return self.oyunDevam_mı


    ##
    ## Sol yazıldıgında calısacak kodlar
    ##

    def tekSatırSolaKaydır(self,i,j):
         if self.oyunAlanı[i][j]==0:
             self.oyunAlanı[i][j] = self.oyunAlanı[i][j+1]
             self.oyunAlanı[i][j+1]=0

    def solaTopla(self,i,j):
        if self.oyunAlanı[i][j]==self.oyunAlanı[i][j+1] and self.oyunAlanı[i][j]!=0 :
            self.oyunAlanı[i][j]*=2
            self.oyunAlanı[i][j+1]=0

    def tumSatırları_SolaKaydır(self):
        for i in range(self.matrisBoyutu):
            for a in range (2):

                for j in range (self.matrisBoyutu-1):
                   self.solaTopla(i,j)

                for j in range (self.matrisBoyutu-2,-1,-1):
                    self.tekSatırSolaKaydır(i,j)

        self.rastgele_DegerAta(1)
        self.oyunAlanıYazdır()
        print()

        
    ##
    ## Sag yazıldıgında calısacak kodlar
    ##

    def tekSatırSagaKaydır(self,i,j):
        if self.oyunAlanı[i][j+1]==0:
            self.oyunAlanı[i][j+1] = self.oyunAlanı[i][j]
            self.oyunAlanı[i][j]=0

    def sagaTopla(self,i,j):
        if self.oyunAlanı[i][j+1]==self.oyunAlanı[i][j] and self.oyunAlanı[i][j]!=0:
            self.oyunAlanı[i][j+1]*=2
            self.oyunAlanı[i][j]=0

    def tumSatırları_SagaKaydır(self):
        for i in range(self.matrisBoyutu):
            for a in range(2):
                for j in range (self.matrisBoyutu-2,-1,-1):
                    self.sagaTopla(i,j)
             
                for j in range (self.matrisBoyutu-1):
                    self.tekSatırSagaKaydır(i,j);


        self.rastgele_DegerAta(1)
        self.oyunAlanıYazdır()
        print()


    ##
    ## alt yazıldıgında calısacak kodlar
    ##

    def tekSutunAltaKaydır(self,i,j):
        if self.oyunAlanı[i+1][j]==0:
            self.oyunAlanı[i+1][j] = self.oyunAlanı[i][j]
            self.oyunAlanı[i][j]=0
        
    def altaTopla(self,i,j):
        if self.oyunAlanı[i][j]==self.oyunAlanı[i+1][j] and self.oyunAlanı[i][j]!=0:
            self.oyunAlanı[i+1][j]*=2
            self.oyunAlanı[i][j]=0
            
    def tumSutunları_AsagıKaydır(self):
        for j in range(self.matrisBoyutu):
            for a in range(2):
                for i in range (self.matrisBoyutu-2,-1,-1):
                    self.altaTopla(i,j)

                for i in range (self.matrisBoyutu-1):
                    self.tekSutunAltaKaydır(i,j)

        self.rastgele_DegerAta(1)
        self.oyunAlanıYazdır()
        print()


    ##
    ## ust yazıldıgında calısacak kodlar
    ##

    def tekSutunUsteKaydır(self,i,j):
        if self.oyunAlanı[i][j]==0:
            self.oyunAlanı[i][j] = self.oyunAlanı[i+1][j]
            self.oyunAlanı[i+1][j]=0

    def usteTopla(self,i,j):
        if self.oyunAlanı[i+1][j]==self.oyunAlanı[i][j] and self.oyunAlanı[i][j]!=0:
            self.oyunAlanı[i][j]*=2
            self.oyunAlanı[i+1][j]=0
 
    def tumSutunları_YukarıKaydır(self):
        for j in range(self.matrisBoyutu):
            for a in range(2):

                for i in range (self.matrisBoyutu-1):
                    self.usteTopla(i,j)
                     
                for i in range (self.matrisBoyutu-2,-1,-1):
                    self.tekSutunUsteKaydır(i,j)
               


        self.rastgele_DegerAta(1)
        self.oyunAlanıYazdır()
        print()





#main

_oyun = oyun()
_oyun.oyunAlanıYazdır()
print()


oyunDevam_mı=True
while oyunDevam_mı:

    adım = str(input("yön giriniz (sag/sol/alt/ust): "))
    if adım =="sol":
        _oyun.tumSatırları_SolaKaydır()
    elif adım=="sag":
         _oyun.tumSatırları_SagaKaydır()
    elif adım=="alt":
         _oyun.tumSutunları_AsagıKaydır()
    elif adım=="ust":
         _oyun.tumSutunları_YukarıKaydır()
   
    
    oyunDevam_mı=_oyun.oyunDurum()


input()