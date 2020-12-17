num = int(input("Ingrese un numero para sacar factorial: "))
other = num
Cont = 1

for x in range(2, num + 1):

 Cont = Cont * x
 print(Cont)

print()
print("El factorial de", other, "es:", Cont)