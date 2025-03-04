from time import *
# V5 
# 3.  Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit.
# Tehke algoritm eksamivormi täitmiseks.
for õ in range(20):
    print(f"Soritab eksamit {õ+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

# V4 2. Koostage programmi plokkskeem, 
# et arvutada ainult negatiivsete P antud arvude summa.
#1
summ=0
try:
    P=int(input("Mitu korda kordame?"))
except:
    print("Vale formaat!")
while True:
    try:
        arv=float(input("Sisesta arv: "))
    except:
        print("Vale formaat!")
    if arv<0: summ += arv
    P-=1 
    if P==0:
        break
print(f"Summa: {summ}")
#2
summ=0
try:
    P=int(input("Mitu korda kordame?"))
except:
    print("Vale formaat!")
for i in range(P):
    try:
        arv=float(input("Sisesta arv: "))
        if arv<0: summ += arv
    except:
        print("Vale formaat!")
print(f"Summa: {summ}")
    



#V3 1. Koostage programmi skeem, 
#  mille abil arvutatakse ainult positiivsete arvude summa antud Q arvust.
try:
    Q=int(input("Mitu korda kordame?"))
except:
    print("Vale formaat!")
vastus=0
for i in range(Q):
    try:
        arv=float(input("Sisesta arv:"))
        if arv>0: vastus+=arv
    except:
        print("Vale formaat")
print(f"Summa arved: {vastus}")

#V1 4. Koostage plokkskeem kotlette praadiva roboti jaoks.
try:
    kokku=int(input("Kokku kotlete: "))
    panni_maht=int(input("Panni maht: "))
except: 
    print("Vale formaat!")
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0 : lahenemine+=1
print(f"Praeme. Tuleb {lahenemine} lahenemist.")
for i in range(lahenemine):
    if jaak>0 and i==lahenemine-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {panni_maht} kotlet.")
    print(f"{i+1}. Lahenemine. Praeme esimene pool")
    sleep(aeg)
    print("Ümberpöörame")
    print(f"{i+1}. Lahenemine. Praeme teine pool")
    sleep(aeg)
    print(f"Valmis!")
print("Kõik kotletid on praetud!")

nj