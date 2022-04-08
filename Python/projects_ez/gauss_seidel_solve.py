import numpy as np
A = np.array([[3,-9,5,2,2],[9,-3,-8,-2,4],[-5,4,4,2,6],[4,7,7,5,8],[4,4,5,1,5]])#matriz A
b = np.array([-15,69,-80,-112,-59])# vector b
'''x = np.zeros_like(b) #se le da valores iniciales a x
N = 100 #cuántas iteraciones van haber
print("Matriz",A)
print("Vector",b)
for k in range (N):
    for i in range(len(b)):
        x[i]=(b[i]-np.sum(A[i][:i]*x[:i])-np.sum(A[i][i+1:]*x[i+1:]))/A[i][i]
    e = np.linalg.norm(A@x-b)
    print(k,x,e)
    if e<1e-6:
        break'''
x = np.linalg.solve(A,b)
print(x)        