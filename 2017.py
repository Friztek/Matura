import collections
plik = open("dane.txt")
dane = []
for linika in plik:
    pomoc = linika.split()
    dane.append(pomoc)

def zad1():
    mini, maxi = 1000, -1000
    for linika in dane:
        for liczba in linika:
            if int(liczba) > maxi:
                maxi = int(liczba)
            elif int(liczba) < mini:
                mini = int(liczba)
    print(mini,maxi)

def zad2():
    wynik = 0
    for linika in dane:
        if linika != linika[::-1]:
            wynik+=1
    print(wynik)

def zad3():
    wynik = 0
    for y in range(200):
        for x in range(320):
            warunek = False
            if x>0:
                if abs(int(dane[y][x]) - int(dane[y][x-1])) > 128:
                    warunek = True
            if x<319:
                if abs(int(dane[y][x]) - int(dane[y][x+1])) > 128:
                    warunek = True
            if y>0:
                if abs(int(dane[y][x]) - int(dane[y-1][x])) > 128:
                    warunek = True
            if y<199:
                if abs(int(dane[y][x]) - int(dane[y+1][x])) > 128:
                    warunek = True
            if warunek:
                wynik += 1
    print(wynik)

def zad4():
    maxi = 0
    for _ in range(320):
        pomoc = []
        for x in range(200):
            pomoc.append(dane[x][0])
        pomoc.sort()
        counter = collections.Counter(pomoc)
        _ , largest = counter.most_common(1)[0]
        if largest > maxi:
            maxi = largest
    print(maxi)

