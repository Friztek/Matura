import math
plik = open("punkty.txt")
plik1 = open("wynik_4.txt","w")
x, y = [], []
for linika in plik:
    pomx, pomy = linika.split()
    x.append(int(pomx))
    y.append(int(pomy))

def zad1():
    wynik = 0
    for i in range(len(x)):
        if (x[i]-200)**2 + (y[i]-200)**2 == 200**2:
            print(x[i],y[i])
        elif (x[i]-200)**2 + (y[i]-200)**2 < 200**2:
            wynik+=1
    print(wynik)

def zad2pom(ile):
    nalezaceDoKoła = 0
    for i in range(ile):
        if (x[i]-200)**2 + (y[i]-200)**2 <= 200**2:
            nalezaceDoKoła += 1
    return nalezaceDoKoła

def zad2():
    # pi * 200 * 200        PI
    # --------------    =  ---
    # 400 * 400             4
    nalezace = zad2pom(1000)
    print(nalezace*4/1000)
    nalezace = zad2pom(5000)
    print(nalezace*4/5000)
    nalezace = zad2pom(10000)
    print(nalezace*4/10000)

def zad3():
    pib = math.pi
    for i in range(1,1701):
        nalezace = zad2pom(i)
        plik1.write(str(abs(pib-nalezace*4/i)))
        plik1.write("\n")


zad3()