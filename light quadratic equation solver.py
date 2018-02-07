#calculadora ecuaciones segundo grado simple
valor2= int(input("valor x^2 " ))
valor1= int(input("valor x^1 " ))
valor0= int(input("valor x " ))



raiz1=((valor1**2)-4*valor2*valor0)**(1/2)
resultado1=(-valor1+raiz1)/(2*valor2)

print("resultado 1: ",resultado1)

raiz2=((valor1**2)-4*valor2*valor0)**(1/2)
resultado2=(-valor1-raiz2)/(2*valor2)

print("resultado 2: ",resultado2)

input("pulsa enter para salir")
