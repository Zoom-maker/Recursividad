# GCD(x, y) -> y == 0 ? x : GCD(y, x % y);
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: ")) 
c = True

while (c):

 if (a !=0) & (b != 0):

  # Creamos una variable intermedio que guarde el valor de b;
  d = b 
  b = a % b 
  a = d 

 # En este punto los valores se intercambian 
 # a se convierte en b y b se combierte en el modulo de a entre b
 
 else:

  print()
  print("El Maximo Comun Divisor es: ", a)
  break
