def function(x):
    if x < 1 and x >= 0:
        return -1 + 1.80861*x + 0.19139*x*x*x
    elif x < 2 and x >= 1:
        return 1.14833 -4.63636*x + 6.44498*x*x -1.95694*x*x*x
    elif x < 3 and x >= 2:
        return -51.59809 + 74.48325*x - 33.11483*x*x + 4.63636*x*x*x
    elif x < 4 and x >= 3:
        return 224.47368 -201.58852*x + 58.90909*x*x -5.58852*x*x*x
    elif x < 5 and x >= 4:
        return -307.12440 + 197.11005*x -40.76555*x*x + 2.71770*x*x*x

  
print(round(function(1.5),5))

def zad2():
    maxi, maxix = 0, 0
    for i in range(5000):
        pomoc = i / 1000
        if function(pomoc) > maxi:
            maxi, maxix = function(pomoc), pomoc
    print(round(maxi,5),maxix)

def zad3():
    miejscaZerowe = []
    for i in range(5000000):
        pomoc = i / 1000000
        if round(function(pomoc),5) == 0:
            miejscaZerowe.append(round(pomoc,5))
    print (miejscaZerowe)

zad2()