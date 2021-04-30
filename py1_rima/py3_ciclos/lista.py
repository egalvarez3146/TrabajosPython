def llena_lista_1(A,B):
  
  n=len(A)//2
  C=[]
  for i in range(n):
      d= pow(A[i+1],2)*B[2*i]
      e=A[i]*d
      f=e+B[n+i]
      C.append(f)
      return C
      print(C)
      

