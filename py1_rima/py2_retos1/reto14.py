def cuadrado(z):
  resultado=[]
  for i in range(-z,z+1):
    resultado.append(i**2)
  return(resultado)
def fin():
  print('Programa finalizado')
print(cuadrado(10))
fin()