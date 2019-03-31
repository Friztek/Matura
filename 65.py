plik = open("dane_ulamki.txt", "r")

tab1,tab2 = [], []
for liczba in plik:
    a,b=liczba.split()
    tab1.append(a)
    tab2.append(b)

def zad1():
    mini=10000
    for i in range(len(tab1)):
        pomoc = int(tab1[i])/int(tab2[i])
        if pomoc<mini:
            mini = pomoc
            a = tab1[i]
            b = tab2[i]
    print(mini, a, b)

def zad23():
    odpowiedz2 = 0
    odpowiedz3 = 0
    for i in range(len(tab1)):
        pomoc = 2
        warunek = True
        while pomoc <= int(tab1[i]) or pomoc <= int(tab2[i]):
            if int(tab1[i])%pomoc==0 and int(tab2[i])%pomoc==0:
                warunek = False
                tab1[i]=int(tab1[i])/pomoc
                tab2[i]=int(tab2[i])/pomoc
            else:
                pomoc+=1
        if warunek:
            odpowiedz2+=1
        odpowiedz3 += int(tab1[i])
    print(odpowiedz2, odpowiedz3)

def zad4():
    pomoc = 2*2*3*3*5*5*7*7*13
    wynik_licznik = 0
    for i in range(len(tab1)):
        dzielnik = pomoc/int(tab2[i])
        licznik = int(tab1[i])*dzielnik
        wynik_licznik+=licznik
    print(int(wynik_licznik))

zad4()