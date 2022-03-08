#fonte: https://www.youtube.com/watch?v=LBMguDK0xBw&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=18

#Modificando um Dicionário

alien = {}

alien['cor'] = 'verde'
alien['pontos'] = 5
alien['veloc'] = 'alta'
alien['x_pos'] = 7
alien['y_pos'] = 25

print(f"A posição x do alien é {alien['x_pos']} ")
if alien['veloc'] == 'baixa':
    x_incr = 1
elif alien['veloc'] == 'media':
    x_incr = 2
else:
    x_incr = 3

#Incrementando o valor de um valor do dicionário, dependendo da cadeia de condições acima....
alien['x_pos'] = alien['x_pos'] + x_incr

print(f"A nova posição x do alien, após o incremento é  {alien['x_pos']} ")




