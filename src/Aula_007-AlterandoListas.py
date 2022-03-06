#fonte: https://www.youtube.com/watch?v=WbC8NqvWl_E&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=7

#Alterando e adicionando itens de uma lista
lstlinguagens = ['python', 'c', 'java']
print(lstlinguagens)

lstlinguagens[0] = 'ada'
print(lstlinguagens)

lstlinguagens.append('cobol')
print(lstlinguagens)

#usando metodo extend para incluir mais de um elemento de uma vez em uma lista
lstlinguagens.extend(['cobol', 'pyspark', 'visual basic'])
print(lstlinguagens)

#exluindo um elemento de uma lista e armazenar em uma variável
removido = lstlinguagens.pop(3)
print(f"Item removido :  {removido}")
print(lstlinguagens)

#removendo um item pelo nome do elemento, sem ser pelo indice
removido2 = lstlinguagens.remove('cobol')
print(f"Item removido pelo nome :  {removido2}") #como o remove nao retorna o item removido a variavel fica com none (sem conteúdo)
print(lstlinguagens)







