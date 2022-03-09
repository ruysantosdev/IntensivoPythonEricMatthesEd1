#fonte:https://www.youtube.com/watch?v=zOkJrQabGag&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=23

#Dicionário de Listas

#Enquete de quais linguagens uma determinada pessoa gosta.
respostas = {
    'joao':['python', 'ada'],
    'maria':['python', 'ada', 'c', 'go', 'java'],
    'jose':['ruby'],
}

#For encadeado buscando os itens do dicionário com o método .items.
#como o valor é uma lista e não um item único, precisamos ter um outro laço for
#para que possamos percorrer a lista para cada idem da lista de valores.
# Forma de navegação:
# 1 - Navegar no dicionário, - Primeiro FOR
# 2 - Para cada chave do dicionário navegar na lista - Segundo FOR

print("--------------------------------------------")
print(" ENQUETE DE LINGUAGENS QUERIDAS POR PESSOAS ")
print("--------------------------------------------")
for nome, linguagens in respostas.items():
    print(f"\n{nome.title()} gosta de : ")
    for linguagem in linguagens:
        print(f" - {linguagem}")

#Construir mais três exemplos para treinar o conceito e absorver o conteúdo.

#Caracteriticas de raças de cachorros

raca_caracteristica = {
   'salsichina': ['pequeno porte', 'patas curtas', 'origem alema', 'arteiro', 'apegado com donos', 'bravo com visitas'],
   'pastor alemao': ['grande porte', 'patas longas', 'origem alema', 'cao de guarda','bravo'],
   'fox paulistinha': ['pequeno porte', 'patas curtas', 'origem europeia + paulista da gema :)', 'latidor'],
   'pug': ['pequeno porte', 'patas curtas', 'origem chines', 'arteiro', 'bom para brincar com criancas']
}
print("------------------------------------------------------")
print(" RAÇAS DE CACHORROS E SUAS PRINCIPAIS CARACTERÍSTICAS ")
print("------------------------------------------------------")
for raca, caracteristicas in raca_caracteristica.items():
    print(f"\nA raça {} possui as seguintes características :")
    for caracteristica in caracteristicas:
        print(f"- {caracteristica} ")


