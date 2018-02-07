#calculadora ecuaciones segundo grado simple
valor2= int(input("number x^2 " ))
valor1= int(input("number x^1 " ))
valor0= int(input("number x " ))

raiz1=((valor1**2)-4*valor2*valor0)**(1/2)
resultado1=(-valor1+raiz1)/(2*valor2)

print("result 1: ",resultado1)

raiz2=((valor1**2)-4*valor2*valor0)**(1/2)
resultado2=(-valor1-raiz2)/(2*valor2)

print("result 2: ",resultado2)

input("press enter to exit")
