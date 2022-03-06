#fonte: https://www.youtube.com/watch?v=VoQgpCHD160&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=9

#Percorrendo uma lista com FOR
lstMateriasEscritorio = ['papel sufite', 'caneta', 'lapis', 'marca texto', 'regua']
print("*****************************************")
print(f" Temos os seguintes materiais de escritório no nosso estoque:")
for MaterialEscritorio in lstMateriasEscritorio:
    print(f" \t - {MaterialEscritorio}")

print("*****************************************")

#incluindo mais itens na lista
lstMateriasEscritorio.append('pilha')
print(f"Incluindo pilha na lista : {lstMateriasEscritorio } ")

for MaterialEscritorio in lstMateriasEscritorio:
    print(f" \t - {MaterialEscritorio}")

