#fonte: https://www.youtube.com/watch?v=_FCXSkkEL88&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=22

#Lista de Dicionários


alien_0 = {'cor':'verde', 'pontos':5}
alien_1 = {'cor':'amarelo', 'pontos':10}
alien_2 = {'cor':'vermelho', 'pontos':15}

print("---------------------------------------------------")
aliens = [alien_0, alien_1, alien_2]
print("---------------------------------------------------")
print(aliens)

for alien in aliens:
    print(alien)
print("---------------------------------------------------")

#Criando 30 aliens (dicionários) com a mesma configuracao (cor, e pontos)
for numero in range(30):
    alien = {'cor':'verde', 'pontos':5, 'pos_x':7, 'pos_y':27, 'veloc': 'baixa'}
    aliens.append(alien)
    print(alien)
print("---------------------------------------------------")

#Printando a lista de aliens após a criação:
#contador de aliens
x = 0
for alien in aliens:
    # Criando numerador para cada Alien
    x = x + 1
    print(f" Alien  {x} ==>  {alien}")

print("---------------------------------------------------")
print("     LISTA ATUALIZADA DOS ALIENS ALTERADOS         ")
print("---------------------------------------------------")
#Alterando os 3 primeiros aliens para amarelo com pontuiação = 10

#Printando a lista de aliens novamente, após alteração:
#contador de aliens
x = 0
for alien in aliens[0:3]:
    alien['cor'] = 'amarelo'
    alien['pontos'] = '10'
    alien['veloc'] = 'media'
    alien['pos_x'] = 1
    alien['pos_y'] = 30
    # Criando numerador para cada Alien
    x = x + 1
    print(f" Alien  {x} ==>  {alien}")

#Alterando a posicao do aliens de velociade = baixa eu adiono 1 na posicao x e se for media add 2, alta add 3
#Estava dando o erro  == Traceback (most recent call last) + key error
#pois estava tentando alterar uma chave inexistente para os aliens alterados na linha 39 que não possuiam posicao x

for alien in aliens:
    if alien['veloc'] == 'baixa':
        alien['pos_x'] = alien['pos_x'] + 1
    elif alien['veloc'] == 'media':
        alien['pos_x'] = alien['pos_x'] + 2
    else:
        alien['pos_x'] = alien['pos_x'] + 3

print("---------------------------------------------------")
print(f"O total de aliens da na lista de aliens é : {len(aliens)}")

print("---------------------------------------------------")
print("   LISTA COMPLETA  DOS ALIENS APÓS ATUALIZAÇÃO !!! ")
print("---------------------------------------------------")

#Printando a lista completa de  aliens após a criação:
#contador de aliens
x = 0
for alien in aliens:
    # Criando numerador para cada Alien
    x = x + 1
    print(f" Alien  {x} ==>  {alien}")
print("---------------------------------------------------")
print(f"O total de aliens da na lista de aliens é : {len(aliens)}")