import math
plik = open("NAPIS.TXT")
napisy = []
for linika in plik:
    napisy.append(linika[:-1])

def czyPierwszy(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True


def zad1():
    wynik = 0
    for wyraz in napisy:
        suma = 0
        for litera in wyraz:
            suma += ord(litera)
        if (czyPierwszy(suma)):
            wynik+=1
    print(wynik)

def zad2():
    wynik = []
    for wyraz in napisy:
        warunek = True
        for x in range(len(wyraz)-1):
            if ord(wyraz[x]) >= ord(wyraz[x+1]):
                warunek = False
        if (warunek):
            wynik.append(wyraz)
    print(wynik)

def zad3():
    pom1, pom2 = [], []
    for wyraz in napisy:
        if wyraz in pom1:
            pom2.append(wyraz)
        if wyraz not in pom1:
            pom1.append(wyraz)

    print(pom2)

zad3()
