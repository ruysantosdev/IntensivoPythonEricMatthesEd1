#fonte: https://www.youtube.com/watch?v=dIhVdlWJSUY&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=8
lstComidas = ['arroz', 'feijao', 'batata', 'macarrão']
print(f"Lista original :  {lstComidas}")
print("*****************************************")

#Ordenando listas de forma alphabetica , ascendente e descendente
lstComidas.sort()
print(f"Lista original sorteada alphabeticamente :  {lstComidas}")
print("*****************************************")

lstComidas.sort(reverse=True)
print(f"Lista original sorteada de forma reversa :  {lstComidas}")
print("*****************************************")

#Ordenando listas de maneira temporária, sem impactar a lista original
lstComidas = ['arroz', 'feijao', 'batata', 'macarrão']
print(f"Lista original   :  {lstComidas}")
print(f"Lista temporária sorteada  de forma ascendente :  {sorted(lstComidas)}")
print(f"Comprovanto que ista original se mantem   :  {lstComidas}")
print("*****************************************")

lstComidas2 = sorted(lstComidas,reverse=True)
print(f"Capturando lista temporárica  sorteada de forma descendente em uma nova lista   :  {lstComidas2}")
print("*****************************************")

#Obtendo o tamanho da lista (quantidade de itens armazenados na lista)
lstComidas2.extend(['milho', 'beterraba' , 'pepino'])
print(f"Lista com novos itens   :  {lstComidas2}")
print("*****************************************")
print(f"Descobrindo a quantidade de itens de uma lista :  {len(lstComidas2)}")
print("*****   INCUINDO NOVOS ITEM NA LISTA E PEGANDO NOVO TAMANHO  **************")
lstComidas2.extend(['tomilho', 'cheiro verde' , 'alho'])
print(lstComidas2)
print(f"Descobrindo a quantidade de itens de uma lista (de novo)  :  {len(lstComidas2)}")
print("*****************************************")

