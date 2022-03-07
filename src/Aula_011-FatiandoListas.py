#fonte: https://www.youtube.com/watch?v=2QI3I-7N5cU&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=11

#Consumir parte de uma lista
# --MARC001 -  x = lstLista = [indice_inicial : indice_final+1]
# caso queira pegar uma lista partindo de um índice inicial até o final podemos colocar 0 na segunda parte que entende
# que vai ir até o final da lista, exemplo:  pegar do terceiro item até o final x = lstLista[3:0]
# se nao informar o indice inicial o python entende que será do início (assume 0) x = lstLista[:1]

lstFrutas = ['banana', 'maça', 'pera', 'uva', 'bergamota']

print(f"Consumir parte de uma lista lstFrutas = {lstFrutas} ")

lstDuasPrimeirasFrutas = lstFrutas[0:2]
print(f"Duas primeiras frutas  = {lstDuasPrimeirasFrutas} ")

lstSegunda_e_TerceiraOcorr = lstFrutas[1:3]
lstDuasUltimasFrutas = lstFrutas[3:5]
print(f"Duas segunda e terceira ocorrência  = {lstSegunda_e_TerceiraOcorr} ")

# --MARC001 - Pegando duas últimas ocorrências da lista, informar indice inicial e final somando +1 (termina na 4 ocorr
# mas colocamos uma 5 ocorr para pegar de forma correta.
lstDuasUltimasFrutas = lstFrutas[3:5]
print(f"Duas últimas frutas  = {lstDuasUltimasFrutas} ")


print("-----------------------------------------------------------------------")

print(f"Duas primeiras frutas da lista são : ")
for fruta in lstFrutas[0:2]:
    print(f" - {fruta}")
print("-----------------------------------------------------------------------")

print(f"Duas últimas frutas da lista são : ")
for fruta in lstFrutas[3:5]:
    print(f" - {fruta}")
print("-----------------------------------------------------------------------")

print(f"A terceira e quarta ocorrência da lista são : ")
for fruta in lstFrutas[2:4]:
    print(f" - {fruta}")
print("-----------------------------------------------------------------------")

