import matplotlib.pyplot as plt
import math as m

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

rangeX = [0, 0] #zakres OX
rangeX[0] = int(input('Podaj zakres dolny osi OX: ')) #Podajemy wartość dolną i po spacji wartość górną osi OX
rangeX[1] = int(input('Podaj zakres gorny osi OX: ')) #Podajemy wartość dolną i po spacji wartość górną osi OX

rangeY = [0, 0] #zakres OY
rangeY[0] = int(input('Podaj zakres dolny osi OY: ')) #Podajemy wartość dolną i po spacji wartość górną osi OX
rangeY[1] = int(input('Podaj zakres gorny osi OY: ')) #Podajemy wartość dolną i po spacji wartość górną osi OX

tab = [[], []]

x1 = 0
x2 = 0
counter = 0

#obliczanie delty
dx = b**2-4*a*c
# obliczanie miejsc zerowych
if dx == 0:
    x1 = (-b) / (2 * a)
    plt.plot(x1, 0, 'd')
elif dx > 0:
    x1 = ((-b) - m.sqrt(dx)) / (2 * a)
    plt.plot(x1, 0, 'd')
    x2 = ((-b) + m.sqrt(dx)) / (2 * a)
    plt.plot(x2, 0, 'd')

for x in range(rangeX[0]*10, rangeX[1]*10+1):
    z = x*0.1 #zwiększenie dokładności wykresu
    tab[0].append(z)
    tab[1].append(a * (z ** 2) + b*z + c)
    #sprawdzenie czy dla podanego przez uzytkownika zakresu funkcji będzie widzialna
    if (rangeX[0] <= tab[0][-1] <= rangeX[1]) and (rangeY[0] <= tab[1][-1] <= rangeY[1]):
        counter += 1
#Jeżeli żaden z punktów należących do wykresu nie należy do przedziału w jakim jest wyświetlany wykres, zakończ program
if counter == 0:
    print('Podano zly zakres wykresu. \nZaden z punktow funkcji nie bedzie widoczny na wykresie.')
    quit()
print(dx, x1, x2)
print(tab)
print(tab[0][-1])
print('counter', counter)
plt.axis([rangeX[0], rangeX[1], rangeY[0], rangeY[1]])
plt.plot(tab[0], tab[1])

plt.grid(True)
plt.show()
