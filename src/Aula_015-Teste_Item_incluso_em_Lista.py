#fonte: https://www.youtube.com/watch?v=Rfk_T20pYqs&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=15

#Teste de HUM Item incluso em uma lista (ver se um valor esta em uma lista)

print("----------------------------------------------------------------------------------")
print(" TESTE DE UM ELEMENTO EM UMA LISTA (HUM ITEM ")
print("----------------------------------------------------------------------------------")
lstIngredientes = ['peperoni', 'tomate', 'queijo', 'couve', 'abacaxi']
ingrediente_pedido = 'queijo'

if ingrediente_pedido in lstIngredientes:
    print(f"O ingrediente pedido :  {ingrediente_pedido}  consta na lista de ingredientes ")
else:
    print(f"O ingrediente pedido :  {ingrediente_pedido}  NÃO CONSTA na lista de ingredientes ")

#Teste de MAIS DE HUM Item incluso em uma lista (ver se um valor esta em uma lista)
print("----------------------------------------------------------------------------------")
print(" TESTE DE MAIS DE UM ELEMENTO EM UMA LISTA ( VÁRIOS ITEMS ")
print("----------------------------------------------------------------------------------")

lstIngredientes = ['peperoni', 'tomate', 'queijo', 'couve', 'abacaxi']
lstIngrediente_pedido = ['queijo', 'banana', 'couve', 'frango']

print(f" Lista de Ingredientes Disponíveis {lstIngredientes}")
print(f" Lista de Ingredientes Pedidos  {lstIngrediente_pedido}")
print("----------------------------------------------------------------------------------")

#If retorna TRUE se existir pelo menos um item na lista de ingredientes pedidos
#Criou uma variável ingrediente para percorrer dentro do for cada ocorrencia da lista do pedido do cliente
#esta variavel do ingrediente depois de valorada por cada ocorrencia da lista de pedido percorre a lista de ingredientes
#com isso podemos testar no IF e emitir mensagem correspondente.

#Tarefa: Fazer + 3 exercicios de comparação entre listas pois apanhei um pouoco para me acostumar com este tipo de
#criação de variavel no laço do FOR

if lstIngrediente_pedido:
    for ingrediente in lstIngrediente_pedido:
        if ingrediente in lstIngredientes:
            print(f"O ingrediente pedido :  {ingrediente}  consta na lista de ingredientes ")
        else:
            print(f"O ingrediente pedido :  {ingrediente}  NÃO CONSTA na lista de ingredientes ")
else:
    print("Não foi solicitado nenhum ingredimente no seu pedido ... ele está vazio ... ")

#Fazer para consolidar o conhecimento e pratica de comparação entre listas - pendente.
#Lista de Ingredientes de uma omelete
#Lista de equipamentos médicos
#Lista Peças de um carro


