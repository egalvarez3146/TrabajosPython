def sumatoria_1 (A,B,C):

n=len(A)
acum=0
for i in range(n):
  d=A[i] + B[i]
  e=C[i]*d
acum=acum+e
result  = acum + n*n
return result
