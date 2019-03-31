plik = open("binarne.txt")
liczby = []
for linika in plik:
    liczby.append(linika[:-1])

def zad1():
    maxi, wynik, maxin = 0, 0, ""
    for liczba in liczby:
        pom1 = liczba[:int((len(liczba))/2)]
        pom2 = liczba[int((len(liczba)-1)/2)+1:]
        if pom1 == pom2:
            wynik += 1
            if maxi < len(liczba):
                maxi = len(liczba)
                maxin = liczba
    print(wynik, maxi, maxin)
  

def zad2():
    wynik, maxi = 0, 1000000000
    for liczba in liczby:
        warunek = False
        pomoc = int(len(liczba) / 4)
        for x in range(pomoc):
            pomoc1 = liczba[x*4:(x+1)*4]
            if int(pomoc1,2) > 9:
                warunek = True
        if warunek:
            wynik += 1
            if len(liczba) < maxi:
                maxi = len(liczba)
    print(wynik, maxi)

def zad3():
    maxi = 0
    for liczba in liczby:
        pomoc = int(liczba,2)
        if pomoc > maxi and pomoc <= 65535:
            maxi = pomoc 
            wynik = liczba
    print(maxi, wynik)

zad3()
