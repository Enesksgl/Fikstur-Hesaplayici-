import random

import numpy as np
from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter.ttk import Combobox

#Dosyadan takımları alıp listeye atamak 
#-------------------------------------------------------------------

takimdosyasi = open("takimlar.txt","r+",encoding="utf8")
takimlistesistring = takimdosyasi.read();
takimlistesi = takimlistesistring.split("\n")    
takimdosyasi.close()   

#Numpy kullanarak matris oluşturmak 
#-------------------------------------------------------------------

liste = random.sample(range(1,19),18) 

m = np.zeros(shape=(18,18))

m[0][0] = 0

for i in range(1,18):
   
        
    m[0][i]=liste[0]
    liste.remove(liste[0])
    
for i in range(1,17):   
    for j in range(2,17):
        if(j>i):
            m[i][j] = m[i-1][j+1]
    m[i][17]= m[0][i]
    
    
print(m)  

#Numpy kütüphanesindeki transpoze metodu ile transpozesini
#oluşturup +17 veya -17 eklettim
#-----------------------------------------------------------------------  

print(30*"___")
mt = np.zeros(shape=(18,18))
mt = m.transpose().copy()

for i in range(0,18):   
    for j in range(0,18):
        
        if(mt[i][j]==0):
            continue
        elif(mt[i][j]==18):
            mt[i][j]=mt[i][j]-17
        else:
            mt[i][j]=mt[i][j]+17
            
print(mt)

m = m+mt

print(m)

#Hafta seçildikten sonra çalışan ve matristeki ilgili
#terimleri arayıp o değerlerdeki takımları yazdıran fonksıyon
#----------------------------------------------------------------------

def haftasec():
    
    hafta = haftalarlistesikutusu.get()#Comboboxtan veri almak 
    hafta = int(hafta)
    deger = np.argwhere(m == hafta) #Numpyda aratmak 
    
   
    
    maclistesi.delete(0,9) # listbox temizlemek 
    for i in range(0,9):  # satır ve sütunda arama yapmak
        a = deger[i][0]
        a = int(a)
        b = deger[i][1]
        b = int(b)
        macmetni = ("{:>25}".format(takimlistesi[a])+"-----"+"{:<25}".format(takimlistesi[b]))
        print(macmetni)
        # listbox a eklemek için string metin  olusturmak 
        #burda ortadakı çizgilerin hepsının ortada olmasını saglamaya çalıştım 
        #ama listboxta boşluk ve karakterlerin boyutu aynı olmadıgı için istediğimi elde edemedim
        #konsolda çalışıyor
        maclistesi.insert(END,macmetni) #listeye satırı eklemek
        

#Tkinter arayüzünü olusturmak 
#----------------------------------------------------------------------

pencere = Tk() 

pencere.title("Fikstür Programı Enes Köseoğlu 1191602019")

labelhafta = Label( text="Haftalar :", font="Arial", width=10, anchor="e")

labelhafta.grid(row=0, column=0)



haftalarlistesi = list(range(1,35)) #Combobox bu listeyi kullanıyor

haftalarlistesikutusu = Combobox(values =haftalarlistesi,height = 12)#hafta seçilen kısım 
haftalarlistesikutusu.set("Hafta Seçiniz...")
haftalarlistesikutusu.grid(row=0,column = 1)

maclistesi =Listbox(height=20,width=50)

maclistesi.grid(row=1, column=1)

maclaribulbutton = Button(text="Haftanın maçlarını göster",command=haftasec)
maclaribulbutton.grid(row=0, column=2)


pencere.mainloop()







                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
