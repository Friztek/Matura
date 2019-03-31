plik = open("liczby.txt")
liczby = []
for linika in plik:
    liczby.append(linika[:-1])

def zad1():
    wynik = 0
    for liczba in liczby:
        zera, jedynki = 0, 0
        for cyfra in liczba:
            if cyfra == "1":
                jedynki += 1
            elif cyfra == "0":
                zera += 1
        if jedynki < zera:
            wynik += 1
    print(wynik)

def zad2():
    wynik2, wynik8 = 0, 0
    for liczba in liczby:
        print(liczba[len(liczba)-3:])
        if liczba[-1] == "0":
            wynik2 += 1
        if liczba[len(liczba)-3:] == "000":
            wynik8 += 1
    print(wynik2,wynik8)

def zad3():
    decimal = []
    for liczba in liczby:
        decimal.append(int(liczba,2))
    decimal.sort()
    for i in range(len(liczby)):
        if (int(liczby[i],2)) == decimal[0]:
            print(i+1)
        elif (int(liczby[i],2)) == decimal[-1]:
            print(i+1)
