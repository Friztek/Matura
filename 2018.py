plik = open("sygnaly.txt")
sygnaly = []
for linika in plik:
    sygnaly.append(linika)

def zad1():
    wynik = []
    for i in range(39,len(sygnaly),40):
        pomoc = sygnaly[i]
        wynik.append(pomoc[9])
    print(wynik)

def zad2():
    maxi = 0
    for linika in sygnaly:
        linika2 = []
        for litera in linika:
            if litera not in linika2:
                linika2.append(litera)
        if len(linika2) > maxi:
            maxi = len(linika2)
            odpowiedz = linika
    print(odpowiedz, maxi-1)

def zad3():
    wyniki = []
    for linika in sygnaly:
        pomoc = linika[:-2]
        pomoc = ''.join(sorted(pomoc))   
        if abs(ord(pomoc[0]) - ord(pomoc[-1])) > 10:
            continue
        else:
            wyniki.append(linika[:-2])
    print(wyniki)        
zad3()

