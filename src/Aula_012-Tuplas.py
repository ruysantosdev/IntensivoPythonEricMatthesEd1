#fonte: https://www.youtube.com/watch?v=W7iGBjy5ruQ&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=12

#Tuplas
tplPonto = (23,10,17,18,10,79,24,7,76)
print(" --------------------------------------------------------------------------- ")
print(f"Exibindo a tupla tplPonto ==>  {tplPonto} ")
print(" --------------------------------------------------------------------------- ")
print(f"Pegando um elemento de uma Tupla (terceiro elemento) ==>  {tplPonto[2]} ")
print(f"Pegando quarto e quinto elemento da tupla ==>  {tplPonto[3:5]} ")
print(" --------------------------------------------------------------------------- ")
print("Nunca podemos alterar um único elemento de uma tupla mas podemos subistutuir ela por inteiro")
print(f"Exibindo a tupla {tplPonto} ")
print("Substituindo seus elementos para ==> tplPonto = (1,2,3,4,5) ")
tplPonto = (1,2,3,4,5)
print(f" Exibindo a tupla alterada (de forma inteira) ==>  {tplPonto} ")
print(" --------------------------------------------------------------------------- ")

#Percorrento a tupla com um for (usando o mesmo conceito usando com listas

print("Os valores desta tupla são \t : ")
for ponto in tplPonto:
    print(f" - {ponto}")






