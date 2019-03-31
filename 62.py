def zad1():
    liczby.sort()
    print ("zad1: ",liczby[0], liczby[len(liczby)-1])

def zad2():
    maxi = 0
    maxil = 0 
    for i in range(len(liczby1)-2):
        warunek = True
        pomoc = i
        ile = 0 
        while warunek:
            if liczby1[pomoc] <= liczby1[pomoc+1]:
                ile += 1
                pomoc += 1
            else:
                warunek = False  
                if ile > maxi:
                    maxi = ile
                    maxil = liczby1[i]
    maxi+=1
    print ("zad2: ",maxil, maxi)

def zad3():
    liczbydec = []
    pom1,pom2 = 0,0
    for liczba in liczby:
        liczbydec.append(int(str(liczba), 8))
    for i in range(1000):
        if liczbydec[i]==liczby1[i]:
            pom1+=1
        elif liczbydec[i]>liczby1[i]:
            pom2+=1
    print("zad3: ",pom1,pom2)

def zad4():
    pom1 = 0
    for liczba in liczby1:
        print(liczba)
        pomoc = str(liczba)
        for l in pomoc:
            if l=="6":
                pom1+=1
        print(pom1)
        #nie skonczone
    


plik = open("liczby1.txt", "r")
plik1 = open("liczby2.txt", "r")
liczby,liczby1 = [],[]
for liczba in plik:
    liczby.append(int(liczba))
for liczba in plik1:
    liczby1.append(int(liczba))

zad3()
zad1()
zad2()
zad4()




    
