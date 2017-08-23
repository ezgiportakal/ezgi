import random

semboller = ["Sinek","Kupa","Maça","Karo"]
sayilar = [1,2,3,4,5,6,7,8,9,10,"Joker","Kız","Papaz"]
kagitlar=[]

for sembol in semboller:
    for sayi in sayilar:
        kagitlar.append(sembol + " " + str(sayi) )

oyuncular={}

for oyuncu in range(1,5):
    oyuncular["Oyuncu " + str(oyuncu)] = []
    for dagit in range(1,4):
        kagit = kagitlar.pop(kagitlar.index(random.choice(kagitlar)))
        oyuncular["Oyuncu "+ str(oyuncu)].append(kagit)

for x in sorted(oyuncular):
    print (x + "\n")
    for y in oyuncular[x]:
        print (y)
