plik = open("dane_napisy.txt","r")
tab1, tab2 = [], []
for linika in plik:
    a,b = linika.split()
    tab1.append(a)
    tab2.append(b)

def zad1():
    wynik = 0
    for i in range(len(tab1)):
        warunek = True
        pomoc1, pomoc2 = tab1[i], tab2[i]
        if pomoc1==pomoc2:
            for x in range(len(pomoc1)-1):
                if pomoc1[x]!=pomoc1[x+1]:
                    warunek = False
                    break
        else:
            warunek = False
        if (warunek):
            wynik+=1
    print(wynik)

def zad2():
    wynik = 0
    for i in range(len(tab1)):
        pomoc1, pomoc2 = tab1[i], tab2[i]
        p1, p2 = sorted(pomoc1), sorted(pomoc2)
        if p1==p2:
            wynik+=1
    print(wynik)

def zad3():
    tab, tabS, wynik = tab1 + tab2, [], 0
    for i in range(len(tab)):
        pomoc = tab[i]
        tabS.append(sorted(pomoc))
    for i in range(len(tabS)):
        count = 0
        pomoc = tabS[i]
        for x in range(i,len(tabS)):
            if pomoc==tabS[x]:
                count +=1
        if count>wynik:
            wynik = count
    print (wynik)

zad1()
zad2()
zad3()