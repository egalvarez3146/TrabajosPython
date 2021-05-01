A=[1,2,3,4]
B=[5,6,7,8]
n=len(A)//2
[(pow(A[i+1],2)*B[2*i])+B[n+i] for i in range(n)]
