
x = int(input("¿Ingrese el año?"))
def bisiesto(x):
  if x%4==0:
    if x%100==0:
      if x%400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
if bisiesto(x):
  print(x,'es un año bisiesto.')
elif not(bisiesto(x)):
  print(x,'no es un año bisiesto')