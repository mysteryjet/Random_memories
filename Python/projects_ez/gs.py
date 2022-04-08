from errno import EROFS, errorcode


x1old = 0
x2old=0
x3old=0
x4old=0
x5old=0
x1new=0
x2new=0
x3new=0
x4new=0
x5new=0
c1=float(input("Ingresa el coeficiente: "))
c2=float(input("Ingresa el coeficiente: "))
c3=float(input("Ingresa el coeficiente: "))
c4=float(input("Ingresa el coeficiente: "))
c5=float(input("Ingresa el coeficiente: "))
c6=float(input("Ingresa el coeficiente: "))
c7=float(input("Ingresa el coeficiente: "))
c8=float(input("Ingresa el coeficiente: "))
c9=float(input("Ingresa el coeficiente: "))
c10=float(input("Ingresa el coeficiente: "))
c11=float(input("Ingresa el coeficiente: "))
c12=float(input("Ingresa el coeficiente: "))
c13=float(input("Ingresa el coeficiente: "))
c14=float(input("Ingresa el coeficiente: "))
c15=float(input("Ingresa el coeficiente: "))
c16=float(input("Ingresa el coeficiente: "))
c17=float(input("Ingresa el coeficiente: "))
c18=float(input("Ingresa el coeficiente: "))
c19=float(input("Ingresa el coeficiente: "))
c20=float(input("Ingresa el coeficiente: "))
c21=float(input("Ingresa el coeficiente: "))
c22=float(input("Ingresa el coeficiente: "))
c23=float(input("Ingresa el coeficiente: "))
c24=float(input("Ingresa el coeficiente: "))
c25=float(input("Ingresa el coeficiente: "))
t1=float(input("Ingresa el termino independiente: "))
t2=float(input("Ingresa el termino independiente: "))
t3=float(input("Ingresa el termino independiente: "))
t4=float(input("Ingresa el termino independiente: "))
t5=float(input("Ingresa el termino independiente: "))
error=float(input("Ingresa el error máximo permitido: "))
iteracion=int(input("Ingresa el numero máximo de iteraciones: "))
rx1=0
rx2=0
rx3=0
rx4=0
rx5=0
fin = False

'''if  (abs(c1)> abs(c2)+abs(c3) and abs(c5)>abs(c4)+abs(c6) and abs(c9)>abs(c7)+ abs(c8)):
    fin = True
    print("Si hay convergencia")
else:
    print("no hay convergencia")'''
n = 0
while (fin==True):
    x1new = (t1 + c2 * x2old - c3 * x3old - c4*x4old - c5*x5old) / c1
    x2new = (t2 - c1 * x1new + c3 * x3old + c4*x4old - c5*x5old) / c2
    x3new = (t3 + c1 * x1new - c2 * x2new - c4*x4old - c5*x5old) / c3
    x4new = (t4 - c1 * x1new - c2 * x2new - c3*x3new - c5*x5old) / c4
    x5new = (t5 - c1 * x1new - c2 * x2new - c3*x3new - c4*x4old) / c5

    rx1 = abs((x1new - x1old) / x1new) *100
    rx2 = abs((x2new - x2old) / x2new) *100
    rx3 = abs((x3new - x3old) / x3new) *100
    rx4 = abs((x4new - x4old) / x4new) *100
    rx5 = abs((x5new - x5old) / x5new) *100

    x1old = x1new
    x2old = x2new
    x3old = x3new
    x4old = x4new
    x5old = x5new

    n =+ 1
    if (n > iteracion or (rx1 < error and rx2 < error and rx3 < error and rx4 < error and rx5 < error)):
        fin= False
print(f"se realizaron un total de: {n} iteraciones")
print(x1old)
print(x2old)
print(x3old)
print(x4old)
print(x5old)

print("\n")
print("{:.20%}".format(rx1))
print("{:.20%}".format(rx2))
print("{:.20%}".format(rx3))
print("{:.20%}".format(rx4))
print("{:.20%}".format(rx5))