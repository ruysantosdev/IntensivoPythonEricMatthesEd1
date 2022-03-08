#fonte:

#Percorrendo as chaves de um dicionário.

#Pessoas que votaram.
respostas = {
    'joao':'python',
    'maria': 'c',
    'carlos': 'ruby',
    'joana': 'python'
}
#Monta lista de pessoas que devem votar.
obrigados_votar = ['joao', 'eduardo', 'jeferson', 'joana']

#Monta lista de pessoas que votaram (ordenado por ordem alphabetica usando o método sorted).
print("--------------------------------------------------------")
for nome in sorted(respostas.keys()):
    print(f" {nome.title()} votou na enquete")
print("--------------------------------------------------------")

#Mostra lista das pessoas obrigadas a votar de forma ordenada aphabeticamente.
for nome in sorted(obrigados_votar):
    print(f"Pessoas obrigadas a votar : {nome.title()}")
print("--------------------------------------------------------")
print(" DAS PESSOAS OBRIGADA A VOTAR QUEM VOTOU E NAO VOTOU  ? ")
print("--------------------------------------------------------")

#Verifica quem votou e quem não votou e emitir mensagem.
for nome in obrigados_votar:
    if nome in respostas.keys():
        print(f"{nome.title()} votou e está tudo OK.")
    else:
        print(f"{nome.title()} NÃO VOTOU e deve justificar o motivo !!")






