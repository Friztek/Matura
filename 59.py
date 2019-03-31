import math
plik = open("liczby.txt","r")
liczby = []
for liczba in plik:
    liczby.append(liczba)

def zad1():
    wynik = 0
    for liczba in liczby:
        n, warunek, czynniki = int(liczba), True, []
        while n % 2 == 0: 
            warunek = False
            n /= 2
        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                if i not in czynniki and i%2!=0:
                    czynniki.append(int(i)) 
                n /= i 
        if n > 2:
            if n not in czynniki and n%2!=0:
                czynniki.append(int(n))

        if len(czynniki)==3 and warunek:
            wynik += 1
    print(wynik)

def zad2():
    wynik = 0
    for liczba in liczby:
        suma = str(int(liczba) + int(liczba[::-1]))
        if suma == suma[::-1]:
            wynik += 1
    print(wynik)

def moc(n):
    wynik = 0
    while n > 9:
        iloczyn = 1
        for i in str(n):
            iloczyn *= int(i)
        n = iloczyn
        wynik += 1
    return wynik

def zad3():
    wynikmoc = [0] * 8
    moc1 = []
    for liczba in liczby:
        pomoc = int(moc(int(liczba)))
        if pomoc == 1:
            moc1.append(int(liczba))
        wynikmoc[pomoc-1] += 1
    moc1.sort()
    print(moc1[0], moc1[-1], wynikmoc)

zad3()


