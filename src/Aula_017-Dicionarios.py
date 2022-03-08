#fonte: https://www.youtube.com/watch?v=aJ-S4IuxIJ4&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=17

#Dicionários
alien_0 = {'cor':'verde','pontos':5}
print(alien_0)

#Exibindo um conteúdo de uma chave do dicionário
print(f" A cor do alien 0 é {alien_0['cor']}")
print(f" Se matar o Alien 0 você ganhará {alien_0['pontos']} pontos")

#Valorando uma variável
pontos = alien_0['pontos']
print(f" Se matar o Alien 0 você ganhará {pontos} pontos")

#Adicionando novos valores em um dicionário existente, caso eu informe um par de chave valor inexistente será criado.
alien_0['pos_x'] = 7
alien_0['pos_y'] = 25
alien_0['nome'] = 'Genivaldo'


print(alien_0)

print("------------------------------------------------------------")
print(f" Seguem os dados do alinen 0 \t")
print(f" - nome    = {alien_0['nome']}")
print(f" - cor     = {alien_0['cor']}")
print(f" - pontos  = {alien_0['pontos']}")
print(f" - pos_x   = {alien_0['pos_x']}")
print(f" - pos_y   = {alien_0['pos_y']}")
print("------------------------------------------------------------")