plik = open("dane_6_1.txt")
plik1 = open("wyniki_6_1.txt","w")
plik2 = open("dane_6_2.txt")
plik3 = open("wyniki_6_2.txt","w")
plik3 = open("dane_6_3.txt")
wyrazy = []
wyrazy1, klucze1 = [], []
for linika in plik:
    wyrazy.append(linika)

for linika in plik2:
    pom1, pom2 = linika.split(" ")
    wyrazy1.append(pom1)
    if len(pom2[:-1]) == 0:
        klucze1.append(0)
    else:
        klucze1.append(int(pom2[:-1]))

slowo1, slowo2 = [], []
for linika in plik3:
    pom1, pom2 = linika.split(" ")
    slowo1.append(pom1)
    slowo2.append(pom2[:-1])

def szyfrowanie(wyraz, klucz):
    wynik = ""
    for litera in wyraz:
        pomoc = ord(litera) - 65
        pomoc += klucz%26
        if pomoc > 25:
            pomoc -= 26
        wynik += (chr(pomoc+65)) 
    return wynik

def szyfrowanie2(wyraz, klucz):
    wynik = ""
    for litera in wyraz:
        pomoc = ord(litera) - 65
        pomoc -= klucz%26
        if pomoc < 0:
            pomoc += 26
        wynik += (chr(pomoc+65)) 
    return wynik

def zad1():
    for wyraz in wyrazy:
        plik1.write(szyfrowanie(wyraz,107))
    
def zad2():
    for i in range(len(wyrazy1)):
        pomoc = (szyfrowanie2(wyrazy1[i],klucze1[i]))
        plik3.write(pomoc)
        plik3.write("\n")

def zad3():
    for i in range(len(slowo1)):
        wyniki = []
        pomoc1 = slowo1[i]
        pomoc2 = slowo2[i]
        for x in range(len(pomoc1)):
            roznica = ord(pomoc1[x]) - ord(pomoc2[x])
            if roznica not in wyniki:
                wyniki.append(roznica)
        if len(wyniki) > 2:
            print(pomoc1)


zad3()



    

