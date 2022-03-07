#fonte:https://www.youtube.com/watch?v=8yYTNVszyks&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=16

#IF THEM ELSE - ELIF NO PYTHON

#Variável idade que armazena a idade do cliente (que irá comprar o ingresso)

print("Informe a idade do cliente : ", end=' ')
idade = int(input())

#De acordo com a idade , vamos definir a variável preço de acordo com o
#valor a ser pago
if idade <= 5:
    preco = 0
elif idade <= 13:
    preco = 5
elif idade <= 18:
    preco = 10
elif idade <= 65:
    preco = 15
else:
    preco = 0

print(f"O preço do seu ingresso, para sua faixa de idade será de :  R$ {preco},00 reais, bom filme !!!")

