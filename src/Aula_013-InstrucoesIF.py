#fonte: https://www.youtube.com/watch?v=JUrbKC0P3Pk&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=13

#Intruções IF
lstEmpresas = ['apple', 'bmw', 'tesla', 'spacex']

print("-------------------------------------------------------------------------------------------")
print(f" Lista de empresa lstEmpresas ==> {lstEmpresas}")
print("-------------------------------------------------------------------------------------------")

print("Usando IF para exibir a lista de empresa com primeira letra maiuscula, mas SE empresa = BMW deve ser tudo MAIÚSCULO")
for empresa in lstEmpresas:
   if empresa == 'bmw':
        print(f"- {empresa.upper()}")
   else:
        print(f"- {empresa.title()}")

print("-------------------------------------------------------------------------------------------")

print("Usando IF com condição de diferente != , se empresa DIFERENTE de spacex colocar 3 *** no final do nome da empresa")
for empresa in lstEmpresas:
   if empresa != 'spacex':
        print(f"- {empresa.title()}***")
   else:
        print(f"- {empresa.title()}")

print("-------------------------------------------------------------------------------------------")


