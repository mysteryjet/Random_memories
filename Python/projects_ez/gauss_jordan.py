#método de gauss jordan

def gaussjordan ():
    import numpy
    n = int(input("Ingresa las variables: "))
    A=numpy.zeros((n, n+1))
    X=numpy.zeros(n)
    print("Ingresa los coeficientes de la matriz aumentada: ")
    for i in range(n):
        for j in range(n+1):
            A[i] [j]= float(input('A['+str(i) + '] [' + str(j) + '] = '))
    print(A)

    for i in range (n):
        if A[i][i] == 0.0:
            print('Divide por cero detectado')
            break
        for j in range(n):
            if i != j:
                r = A[j][i] / A[i][i]
                for k in range(n+1):
                    A[j][k] = A[j][k] - r*A [i][k]
        print("La matriz diagonal es: ")
        print(A)
        print("\nEl valor de las variables son: ")
        for i in range(n):
            X[i]  = A[i][n] / A[i][i]
        for i in range(n):
            print('X%d=%0.2f' % (i, X[i]) , end='\n')

gaussjordan()            


