#fonte: https://www.youtube.com/watch?v=0DZcGK-0bPM&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=5
nome = "ruy santos"
nome2 = "RUY SANTOS"
primeiro_nome = "ruy"
sobrenome = "santos"

#metodo title (usando em string) primeira letra de cada palavra em maiusculo
print(nome.title())

#metodo upper (usando em string) deixa tudo em maiusculo
print(nome.upper())

#metodo lower (usando em string) deixa tudo em minusculo
print(nome2.lower())

print("Meu nome é " + primeiro_nome.title() + " " + sobrenome.title())

#usanso \n como caractere especial de quebra de linha
frase= "Meu computador é um : \n 486 DX2"
print(frase)

#consigo criar esta sting somente em uma linha de código, se quebrar o python reclama, ver meio de rodar isso em mais de uma linha
#sem que não quebre, com o objetivo de deixar mais legível o código
frase2 = "Eu nado os seguintes estilos de natação : \n " +  "\t - craw ou nado livre \n " +  "\t - costas \n " + "\t - peito \n " + "\t - borboleta \n "
print(frase2)

#retirar espaços esquerda , direita e de ambos os lados
string_espacos_esquerda = "     Eu estou apredendendo Python3"
string_espacos_direita = "Eu estou apredendendo Python3      "
string_espacos_ambos = "       Eu estou apredendendo Python3       "
print("string_espacos_esquerda :" + string_espacos_esquerda)
print("string_espacos_direita :" + string_espacos_direita)
print("string_espacos_ambos :" + string_espacos_ambos)
print(" ***** retirando os espaços ******* ")
print( "Retirando espaços a esquerda :"+ string_espacos_direita.lstrip())
print( "Retirando espaços a direira :"+ string_espacos_direita.rstrip())
print( "Retirando espaços em ambos os lados :" + string_espacos_direita.strip())