plik1 = open("dane_systemy1.txt","r")
plik2 = open("dane_systemy2.txt","r")
plik3 = open("dane_systemy3.txt","r")
czas1, temp1, czas2, temp2, czas3, temp3 = [], [], [], [], [], []
for linika in plik1:
    a,b = linika.split()
    czas1.append(a)
    temp1.append(b)

for linika in plik2:
    a,b = linika.split()
    czas2.append(a)
    temp2.append(b)

for linika in plik3:
    a,b = linika.split()
    czas3.append(a)
    temp3.append(b)

def zad1():
    mini1, mini2, mini3 = 0, 0, 0
    for temp in temp1:
        pomoc = int(temp,2)
        if pomoc < mini1:
            mini1 = pomoc
    for temp in temp2:
        pomoc = int(temp,4)
        if pomoc < mini2:
            mini2 = pomoc
    for temp in temp3:
        pomoc = int(temp,8)
        if pomoc < mini3:
            mini3 = pomoc
    print(bin(mini1), bin(mini2), bin(mini3))

def zad2():
    wynik, pomoc = 0, 12
    for i in range(len(czas1)):
        if int(czas1[i], 2) != pomoc and int(czas2[i], 4) != pomoc and int(czas3[i], 8) != pomoc: 
            wynik += 1
        pomoc += 24
    print(wynik)

def zad3():
    maxi1, maxi2, maxi3, wynik = -100, -100, -100, 0
    for i in range(len(temp1)):
        warunek = False
        if int(temp1[i],2) > maxi1:
            warunek = True
            maxi1 = int(temp1[i],2)
        if int(temp2[i],4) > maxi2:
            warunek = True
            maxi2 = int(temp2[i],4)
        if int(temp3[i],8) > maxi3:
            warunek = True
            maxi3 = int(temp3[i],8)
        if (warunek):
            wynik += 1
        warunek = False
    print(wynik)

def zad4():
    maxi = 0
    for i in range (len(temp1)):
        for j in range (len(temp1)-i):
            Rij = (int(temp1[i], 2) - int(temp1[j], 2))**2
            pomoc = abs(i-j)
            if pomoc != 0:
                wynik = Rij / pomoc
                if wynik > maxi:
                    maxi = wynik
    if maxi > int(maxi):
        maxi = int(maxi) + 1
    print(maxi)


        

                