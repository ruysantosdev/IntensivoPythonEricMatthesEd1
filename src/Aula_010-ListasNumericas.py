#fonte: https://www.youtube.com/watch?v=Qiy3VPypqJ8&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=10


lstNumeros = [1,2,3,4,5]
print("-----------------------------------------------------" )
print(f"Lista de numeros de 1 a 5 lstNumeros :  {lstNumeros}" )
print("-----------------------------------------------------" )
print("Usando for com range para gerar numero de 1 a 5 " )
for valor in range (1,6):
    print(valor)

for valor in range (1,21):
    lstNumeros.append(valor)
print(f" Nova lista de numeros de 1 a 20 criada no for : { lstNumeros}")
print("-----------------------------------------------------" )

#Melhor opcão de criar uma lista com numeros usando o método list(range(posicao inicial, tamanho))

lstNumeros1a13 = list(range(1,14))
print(f" Nova lista de numeros de 1 a 13 criada via list(range(posicao inicial, tamanho) : { lstNumeros1a13}")
print("-----------------------------------------------------" )

#Usando parametro de incremento no range (por padrao é 1 mas podemos mudar(onde x = 2) --> list(range(1,20,x))
print("Usando o método list(range(posicao inicial, tamanho, incremento)) | lstNumerosImpares = list(range(1,20,2))")
lstNumerosImpares = list(range(1,20,2))
print(f"Lista de numeros impares ate 20   : { lstNumerosImpares}")
print("-----------------------------------------------------" )

lstNumerosPares = list(range(0,21,2))
print(f"Lista de numeros pares ate 20   : { lstNumerosPares}")
print("-----------------------------------------------------" )