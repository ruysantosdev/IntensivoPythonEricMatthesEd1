#fonte:

#Percorrendo valores de um dicionário

#Pessoas que votaram.
respostas = {
    'joao':'python',
    'maria': 'c',
    'carlos': 'ruby',
    'joana': 'python'
}

#Monta lista dos valores do dicionário, removendo os valores duplicados usando
# a funcao set -->  sorted(set(respostas.values()))

print("--------------------------------------------------------")
print(f"As linguagens presentes neste dicionário são :")
for linguagem in sorted(set(respostas.values())):
    print(f" - {linguagem.title()}")
print("--------------------------------------------------------")

