plik = open("tekst.txt", "r")

for wyraz in plik: 
    tekst = wyraz.split()

def zad1():
    wynik = 0
    for wyraz in tekst:
        for i in range(len(wyraz)-1):
            if wyraz[i]==wyraz[i+1]:
                wynik+=1
                break
    print (wynik)

def zad2():
    litery = []
    ileznakow = 0
    for wyraz in tekst:
        ileznakow += len(wyraz)
        for litera in wyraz:
            if litera not in litery:
                litery.append(litera)
    litery.sort()
    for litera in litery:
        wynik = 0
        for wyraz in tekst:
            for li in wyraz:
                if litera==li:
                    wynik += 1
        print(litera, ": ", wynik, "(", round(wynik*100/ileznakow,2),"%)")       
        print(ileznakow)    

def zad3():
    samogloski, maxi = ["A", "E", "I", "O", "U", "Y"], 0
    for wyraz in tekst:
        wynik = 0
        for litera in wyraz:
            if litera not in samogloski:
                wynik += 1
            else:
                wynik = 0
            if wynik > maxi:
                maxi = wynik
    count = 0
    for wyraz in tekst:
        wynik = 0
        for litera in wyraz:
            if litera not in samogloski:
                wynik += 1
            else:
                wynik = 0
            if wynik == maxi:
                count+=1
                print(wyraz)

zad3()
            