fibbtab = [0,1]
def fibb():
    a, b = 0, 1
    for _ in range(40):
        b, a = b + a, b
        fibbtab.append(b)
fibb()

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def zad1():
    print(fibbtab[10],fibbtab[20],fibbtab[30],fibbtab[40])

def zad2():
    for i in range(3, 40):
        if is_prime(fibbtab[i]):
            print(fibbtab[i])

def zad3():
    fibbbin = []
    for liczba in fibbtab:
        fibbbin.append(int(bin(liczba)[2:]))
    for liczba in fibbbin:
        pom = 0
        for i in str(liczba):
            if i=="1":
                pom+=1
        if pom==6:
            print(liczba)
