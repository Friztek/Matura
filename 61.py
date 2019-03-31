plik = open("ciagi.txt","r")
plik1 = open("bledne.txt","r")
dane, dane1 = [], []
for linika in plik:
    dane.append(linika.split())
for linika in plik1:
    dane1.append(linika.split())

def czyArytmetyczny(ciag):
    roznica = int(ciag[1]) - int(ciag[0])
    for i in range(len(ciag)-1):
        if int(ciag[i+1]) - int(ciag[i]) != roznica:
            return False
    return True

def zad1():
    MaxRoznica, ileCiagow = 0, 0
    for ciag in dane:
        if len(ciag) != 1:
            if czyArytmetyczny(ciag):
                ileCiagow += 1
                if int(ciag[1]) - int(ciag[0]) > MaxRoznica:
                    MaxRoznica = int(ciag[1]) - int(ciag[0])
    print(ileCiagow, MaxRoznica)

def zad2():
    liczby = []
    for ciag in dane:
        if len(ciag) != 1:
            for liczba in ciag:
                if int(round(int(liczba) ** (1 / 3))) ** 3 == int(liczba):
                    liczby.append(liczba)
    print (liczby)

def zad3():
    for ciag in dane1:
        if len(ciag) != 1:
            roznice = []
            for i in range(len(ciag)-1):
                roznica = int(ciag[i+1]) - int(ciag[i])
                roznice.append(roznica)
            for i in roznice:
                if roznice.count(i) > 1:
                    roznica = i
            for i in range(len(roznice)-1):
                if roznice[i] != roznica and roznice[i+1] != roznica:
                    print(ciag[i+1])
                    break
            else:
                print(ciag[-1])

zad3()





