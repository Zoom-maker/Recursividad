num = int(input("Ingrese un numero para mostrar sumatoria: "))
other = num
Cont = 1

for x in range(2, num + 1):

 Cont = Cont + x
 print(Cont)

print()
print("La sumatoria de 1 a", other, "es:", Cont)