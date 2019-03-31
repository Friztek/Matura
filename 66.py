plik = open("trojki.txt","r")
tab1, tab2, tab3 = [], [], []
for linika in plik:
    a,b,c = linika.split()
    tab1.append(a)
    tab2.append(b)
    tab3.append(c)

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def zad1():
    for i in range(len(tab1)):
        pomoc = 0
        for liczba in tab1[i]:
            pomoc+=int(liczba)
        for liczba in tab2[i]:
            pomoc+=int(liczba)
        if pomoc==int(tab3[i]):
            print(tab1[i],tab2[i],tab3[i])
    
def zad2():
    for i in range(len(tab1)):
        if int(tab1[i])*int(tab2[i])==int(tab3[i]):
            if is_prime(int(tab1[i])) and is_prime(int(tab2[i])):
                print(tab1[i],tab2[i],tab3[i])

def zad3():
    for i in range(len(tab1)):
        if (int(tab1[i]))*(int(tab1[i])) + (int(tab2[i]))*(int(tab2[i])) == (int(tab3[i]))*(int(tab3[i])) or (int(tab1[i]))*(int(tab1[i])) + (int(tab3[i]))*(int(tab3[i])) == (int(tab2[i]))*(int(tab2[i])) or (int(tab2[i]))*(int(tab2[i])) + (int(tab3[i]))*(int(tab3[i])) == (int(tab1[i]))*(int(tab1[i])):
            i+=1
            if (int(tab1[i]))*(int(tab1[i])) + (int(tab2[i]))*(int(tab2[i])) == (int(tab3[i]))*(int(tab3[i])) or (int(tab1[i]))*(int(tab1[i])) + (int(tab3[i]))*(int(tab3[i])) == (int(tab2[i]))*(int(tab2[i])) or (int(tab2[i]))*(int(tab2[i])) + (int(tab3[i]))*(int(tab3[i])) == (int(tab1[i]))*(int(tab1[i])):
                i-=1
                print(tab1[i],tab2[i],tab3[i]) 
                print(tab1[i+1],tab2[i+1],tab3[i+1]) 

zad3()