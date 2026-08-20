numero = int (input("Digite um número: "))
resto = numero % 3


if resto == 1:
  print("Seu número é: {}, ele é impar".format(numero))
else:
  print("Seu número é: {}, ele é par".format(numero))

