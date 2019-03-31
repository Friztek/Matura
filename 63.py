plik = open("ciagi.txt","r")
liczby = []
for liczba in plik:
    liczby.append(int(liczba))

def zad1():
    odpowiedz = []
    for liczba in liczby:
        liczba = str(liczba)
        if len(liczba)%2==0:
            a=liczba[0 : int(len(liczba)/2)]
            b=liczba[int(len(liczba)/2):]
            if a==b:
                odpowiedz.append(liczba)
    print (odpowiedz)

def zad2():
    pom1 = 0
    for liczba in liczby:
        liczba = str(liczba)
        if liczba.find("11")==-1:
            pom1 += 1
    print(pom1)

def zad3():
    liczbadec, odpowiedz= [], []
    for liczba in liczby:
        liczbadec.append(int(str(liczba),2))
    for liczba in liczbadec:
        pomoc, ile, i = liczba, 0, 2
        while pomoc>1:
            if pomoc%i==0:
                ile+=1
                pomoc=pomoc/i
                if ile>2:
                    break
            else:
                i+=1
        if pomoc==1 and ile==2:
            odpowiedz.append(liczba)
        odpowiedz.sort()
    print (odpowiedz[0], odpowiedz[len(odpowiedz)-1], len(odpowiedz))

zad3()
