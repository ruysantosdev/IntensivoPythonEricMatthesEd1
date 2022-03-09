#fonte: https://www.youtube.com/watch?v=1GfvOmPNuDM&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=24

#Lista de Dicionário de Lista :P

pedidos = [
    {'espessura': 'grossa',
     'coberturas': [
         'molho de tomate',
         'mussarela',
         'catupiry'
         ]
    },
    {'espessura': 'fina',
     'coberturas': [
         'cebola',
         'catupiry'
     ]
     },
    {'espessura': 'grossa',
     'coberturas': [
         'molho de tomate',
         'mussarela',
         'cebola'
     ]
     }
]

#Percorendo estrutura de dados acima (Lista > Dicionário > Lista)
#Um for para cada nível, observando o tipo de dado , dicionário ou lista.

print("----- Pedidos pendentes para cozinha -----")
for pedido in pedidos:
    print(f"Pedido com massa {pedido['espessura']} : ")
    print(f"\t As coberturas são: ")
    for cobertura in pedido['coberturas']:
        print(f" \t \t - {cobertura}")


#Fazer mais três exemplos com estruturas de dados com mais níveis para consolidar a lógica para percorrer
#estruturas de dados com níveis mais complexos.

