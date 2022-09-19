''' Proyecto para la realización de los ejs:
    7.1    7.2    7.5    7.6  '''


def seteUn () :
    t = (1,2,3,4,5)
    i = 0

    while i < 6:
        print(t[i])
        if i+1 == 5:
            print("La lista está ordenada")
            break

        if t[i]>t[i+1]:
            print("La lista no está ordenada como se desea")
            break
        i +=1

def seteDous(dom1 , dom2):
    i = 0
    cont = 0
    for i in range (2):

        j = 0
        for j in range (2):
            if dom2[j] == dom1[i]:
                print("Es válida")
                cont +=1
                break
            j +=1
        i +=1
    if cont == 0:
        print("No son válidas entre sí")

def seteCinco(num):
    cont=0
    for i in range (1,num):
        if (num%i == 0):
            cont +=1
            if cont > 1:
                return False
    return True

def seteCincodDous(l):
    for i in range(len(l)):
        factorial = l[i]*l[i-1]


seteUn()
seteDous((3,2),(4,5))

lista = [1,2,3,4,5,6,7,8,9,10]
suma=0
for i in lista:
    if seteCinco(i):
        print ("El número "+ str(i) + " es primo.")
    else:
        print ("El número "+ str(i) + " no es primo.")
    suma+=1
print ("La suma de la lista es ", sum(lista))
print ("El promedio de la lista es " , (sum(lista)/len(lista)))