#fonte: https://www.youtube.com/watch?v=N0FLsvsBalg&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=14

#Comparações Numéricas e Testes Condicionais Múltiplos, While , Input  e parametro ,end= '' no print()

#Jogo adivinhe o número segredo
segredo = 73
valor_chute = 18
if valor_chute == segredo:
    print(f"Você acertou o número segredo é extamente  ==> {segredo}")
else:
    print(f"Você erro o número segredo, tente novamente")


#Usando Testes condicionais multiplos de 'IF ENCADEADO' que no python => elif
print("----------------------------------------------------------")
idade = 18
sexo = 'Feminino'

if idade >= 18 and sexo == "Masculino":
    print("Tem que servir se alistar no exercito")
elif idade < 18 or sexo == "Feminino":
    print("Não é necessário se alistar no exercito pois você não tem a idade mínima ou é mulher")
else:
    pass

print("----------------------------------------------------------")

#Dar desconto em entrada do cinema se comprador tiver idade superior a 60 anos
#Usando nova função input() para ler informações recebidas pelo usuário
#usando parametro ,end='' no print() para não pular a linha : exemplo:
#   print("Sua mensagem", end=' ')

print("\n")
print("----------------------------------------------------------")
print("   S I S T E M A  V E N D A  I N G R E S S O  F Á C I L   ")
print("----------------------------------------------------------")
print("\n")

opcao = 'Sim'
while opcao == 'Sim':
    print("Informe a idade do cliente : ", end=' ')
    idade = int(input())
    if idade >= 60:
        print(f"Cliente possui {idade} anos e tem direito a um desconto de  50% no ingresso do cinema :)  ")
    else:
        print(f"Cliente possui  {idade} anos , como não é maior que 60 anos não tem desconto ;( ")
    print("Deseja continuar ? - digite Sim ou Não para sair : ", end=' ')
    opcao = str(input())
    if opcao == 'Sim':
        print("Beleza, processando próximo cliente .... aguarde ....")
    else:
        print("Obrigado por usar nosso sistema de venda de ingressos de cinema :) ")
print("-----------------------------------------------------------")







