plik = open("liczby.txt","r")
liczby = []
for liczba in plik:
    liczby.append(int(liczba))

def zad1():
    wynik, wynikTab = 0, []
    for liczba in liczby:
        if liczba < 1000:
            wynikTab.append(liczba)
            wynik += 1
    print(wynik, wynikTab[-1], wynikTab[-2])

def zad23():
    dzielnikiFull = []
    for liczba in liczby:
        if liczba not in dzielnikiFull:
            dzielnikiFull.append(liczba) 
        dzielniki, pomoc = [], liczba
        for i in range(2, int(liczba/2)+1):
            if pomoc%i==0:
                dzielniki.append(i)
                if i not in dzielnikiFull:
                    dzielnikiFull.append(i) 
        if len(dzielniki)==16:
            print(liczba, dzielniki)
    dzielnikiFull.sort()
        

zad23()




