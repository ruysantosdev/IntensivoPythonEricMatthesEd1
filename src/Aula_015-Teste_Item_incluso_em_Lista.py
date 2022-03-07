#fonte: https://www.youtube.com/watch?v=Rfk_T20pYqs&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=15

#Teste de HUM Item incluso em uma lista (ver se um valor esta em uma lista)

print("----------------------------------------------------------------------------------")
print(" TESTE DE UM ELEMENTO EM UMA LISTA (HUM ITEM)                                     ")
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

#Se lista de lista de ingredientes do pedido  está preenchida (validando se não está vazia)
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
print("----------------------------------------------------------------------------------")
print(" PESQUISA DE ITENS DE UMA LISTA DENTRO DE OUTRA (INTGREDIENTE DE UMA OMELETE)     ")
print("----------------------------------------------------------------------------------")

lstIngredientesOmelete = ['ovo', 'manteiga', 'alho', 'queijo', 'presunto']
lstPedidoOmeleteCliente = ['ovo', 'azeite', 'alho', 'cebola', 'queijo', 'catupiry']

print(f" Lista de ingredientes Omelete ==> {lstIngredientesOmelete}")
print(f" Lista de ingredientes Pedido ==> {lstPedidoOmeleteCliente}")
print("----------------------------------------------------------------------------------")

if lstPedidoOmeleteCliente:
    for ingrediente_omelete in lstPedidoOmeleteCliente:
        if ingrediente_omelete in lstIngredientesOmelete:
            print(f"O ingrediente pedido :  {ingrediente_omelete}  consta na lista de ingredientes da omelete ")
        else:
            print(f"O ingrediente pedido :  {ingrediente_omelete}  NÃO CONSTA na lista de ingredientes da omelete ")
else:
    print("Não foi solicitado nenhum ingredimente de omelete no seu pedido ... ele está vazio ... ")

#Lista de equipamentos médicos
print("----------------------------------------------------------------------------------")
print(" PESQUISA DE ITENS DE UMA LISTA DENTRO DE OUTRA (EQUIPAMENTOS MÉDICOS)            ")
print("  EM UMA LISTA DE EQUIPAMENTOS, BATER COM LISTA DE EQUIPAMENTOS MEDICOS           ")
print("                 INFORMANDO SE O EQUIPAMENTO É MEDICO OU NÃO                      ")
print("----------------------------------------------------------------------------------")

lstEquipamentoMedico = ['luva', 'mascara', 'bisturi', 'atadura', 'gaze']
lstEquipamentos = ['bota', 'lapis', 'luva', 'clips', 'bisturi', 'capacete', 'mascara']

print(f" Lista de Equipamentos Médicos ==> {lstEquipamentoMedico}")
print(f" Lista de ingredientes de Equipamentos ==> {lstEquipamentos}")
print("----------------------------------------------------------------------------------")

#Se lista de equipamentos está preenchida (validando se não está vazia)
if lstEquipamentos:
  for equipamento in lstEquipamentos:
      if equipamento in lstEquipamentoMedico:
          print(f"O equipamento {equipamento}  é um equipamento médico")
      else:
          print(f"O equipamento {equipamento}  NÃO É um equipamento médico")
else:
    print("Lista de equipamentos vazia, não temos condições de comparação com lista de equipamentos médicos, tente de novo")

#Lista Códigos de Produtos dentro do sistema
print("----------------------------------------------------------------------------------")
print(" PESQUISA DE CÓDIGOS DE PRODUTOS LANÇADOS ESTÃO SENDO TRATADOS PELO SISTEMA       ")
print("----------------------------------------------------------------------------------")

lstProdutosNovos = [40512, 62225, 47000, 25690, 89577]
lstProdutosSistema= [12544, 40512, 38720, 47000, 85960, 89577, 25690]

print(f" Lista de Produtos Novos (lançados)        ==> {lstProdutosNovos}")
print(f" Lista de Produtos Tratados pelos Sistema  ==> {lstProdutosSistema}")
print("----------------------------------------------------------------------------------")

# Verificar se lista de produtos novos está preenchida, senao emitir mensagem de erro
if lstProdutosNovos:
    for produto in lstProdutosNovos:
        if produto in lstProdutosSistema:
            print(f"O produto {produto} já é tratado pelo sistema")
        else:
            print(f"O produto {produto} NÃO É TRATADO PELO SISTEMA, PROVIDENCIAR ANALISE E CADASTRAMENTO URGENTE !!!")
else:
    print("Lista de proudtos lançados está vazia, conferir se foi informado os novos produtos e providenciar nova execução")

print("----------------------------------------------------------------------------------")


