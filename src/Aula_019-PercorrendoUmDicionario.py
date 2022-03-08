#fonte: https://www.youtube.com/watch?v=JwfTojt6LzU&list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_&index=19

#Percorrendo um Dicionário

respostas = {
    'joao':'python',
    'maria': 'c',
    'carlos': 'ruby',
    'joana': 'python'
}

print(f"João gosta da linguagem {respostas['joao'].title()}")

#Usando o método .items do dicionário para retornar a chave e o valor para as variáveis criadas no for
print("-------------------------------------------------------------------------")
for nome, linguagem in respostas.items():
    print(f"{nome.title()} gosta da linguagem {linguagem.title()}")
print("-------------------------------------------------------------------------")