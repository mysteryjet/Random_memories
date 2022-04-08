import numpy

m=int(input('Valor de m:'))#m serán los renglones
n=int(input('Valor de n:'))#n serán las columnas
#se declara una matriz que dependerá de los renglones y las columnas que meta el usuario
matrix = numpy.zeros((m,n))
# es donde tendrémos el vector solución
x = numpy.zeros((m))

#se crea un vector que tenga la dimensión n, y se rellena de ceros
vector = numpy.zeros((n))
# se comprueba como se mueven los valores de acuerdo a las iteraciones 
comp = numpy.zeros((m))
# se utilizará una lista  para almacenar el error
error = []

print ('Método de Gauss-Seidel')
print ('Introduce la matriz de coeficientes y el vector solución')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+", "+str(c+1)+"]: "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))

tol = float(input("Cuál es la tolerancia que quieres?: "))# es la tolerancia que el usuario va a querer dar
itera = int(input("Cual es el numero máximo de iteraciones?: ")) #serán las iteraciones que el usuario espera

#método de gauss seidel
k=0 # esto sirve para llevar la cuenta de cuántas vueltas se dan en el ciclo while. servirá para detenerse si los ciclos se exceden
while k < itera:
    suma = 0
    k = k + 1#cada que pase el ciclo, la variable k va contando mas uno al contador
    for r in range(0,m):
        suma = 0
        for c in range(0,n):
            if (c != r):
                suma=suma+matrix[r,c]*x[c]               
        x[r]=(vector[r]-suma)/matrix[r,r] #despeje
        print ("x["+str(r)+"]: "+str(x[r]))
    del error[:]

#comprobación
    for r in range(0,m):
        suma = 0
        for c in range(0,n):
            suma = suma+matrix[r,c]*x[c]
        comp[r] = suma
        dif = abs(comp[r]-vector[r])
        error.append(dif)
        print("Error en x[",r,"]= ",error[r])
    print("Iteraciones: ",k)
    if all(i <= tol for i in error) == True:
        break
print("Terminó el programa.\n")