plik = open("slowa.txt")
slowa1, slowa2 = [], []

for linika in plik:
    pom1, pom2 = linika.split()
    slowa1.append(pom1)
    slowa2.append(pom2)

def zad1():
    wynik = 0
    for slowo in slowa1:
        if slowo[-1] == "A":
            wynik += 1
    for slowo in slowa2:
        if slowo[-1] == "A":
            wynik += 1
    print(wynik)

def zad2():
    wynik = 0
    for i in range(len(slowa1)):
        if slowa1[i] in slowa2[i]:
            wynik += 1
    print(wynik)

def zad3():
    wynik = 0
    for i in range(len(slowa1)):
        pom1, pom2 = slowa1[i], slowa2[i]
        if sorted(pom1) == sorted(pom2) and len(pom1) == len(pom2):
            print(slowa1[i], slowa2[i])
            wynik += 1
    print(wynik)
