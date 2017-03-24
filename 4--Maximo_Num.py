Q=int(input("ingrese un numero\n"))
W=int(input("ingrese otro numero\n"))
E=int(input("ingrese un nuemero\n"))
if(Q > W and Q > E):
 print("El numero Maximo es " + str(Q))
else:
 if(W > Q and W > E):
  print("El numero Maximo es " + str(W))
 else:
  print("El numero Maximo es " + str(E))
  
 input()