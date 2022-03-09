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

#
#Objeto Filmes
#
filmes = [
   {
     'titulo': 'JSON x XML',
     'resumo': 'o duelo de dois modelos de representação de informações',
     'ano': 2012,
     'genero': ['aventura', 'ação', 'ficção']
    },
   {
     'titulo': 'JSON James',
     'resumo': 'a história de uma lenda do velho oeste',
     'ano': 2012,
     'genero': ['western']
    }
]

#
#Objeto Posts de um Blog
#
posts = [
  {
    'post_id': 1,
    'post_descricao': 'Meu post 1',
    'post_titulo': 'Teste',
    'anexos': [
      {
        'anexo_id': 3,
        'anexo_uri': 'img-03.png'
      },
      {
        'anexo_id': 4,
        'anexo_uri': 'img-04.png'
      }
    ]
  },
  {
    'post_id': 3,
    'post_descricao': 'Meu post 2',
    'post_titulo': 'Teste 2',
    ' anexos': [
      {
        'anexo_id': 1,
        'anexo_uri': 'img-01.png'
      },
      {
        'anexo_id': 2,
        'anexo_uri': 'img-02.png'
      }
    ]
  }
]

#
#Objeto Agenda
#
agenda = [
{
    'nome': 'Jose Carlos',
    'sobrenome': 'Macoratti',
    'idade': 45,
    'endereco':  {
                           'endereco': 'Rua Projetada, 200',
                           'cidade': 'Santos',
                           'estado': 'SP',
                           'cep': 11054058
                       },
    'telefone': [
                            {
                                'tipo': 'fixo',
                                'numero': '212 555-1234'
                            },
                            {
                                'tipo': 'celular',
                                'numero': '(55)(11)9.3389-7974'
                            }
                     ]
},

{
    'nome': 'Gabriel Beleleu',
    'sobrenome': 'Beleleu',
    'idade': 45,
    'endereco':  {
                           'endereco': 'Rua Irmãos Piologo, 666',
                           'cidade': 'Cabronro do Norte',
                           'estado': 'SP',
                           'cep': 22054033
                       },
    'telefone': [
                            {
                                'tipo': 'fixo',
                                'numero': '313 555-1234'
                            },
                            {
                                'tipo': 'celular',
                                'numero': '(55)(11)9.5566-8974'
                            }
                     ]
},
{
    'nome': 'Homen Aranha',
    'sobrenome': 'Aranha',
    'idade': 45,
    'endereco':  {
                           'endereco': 'Rua Teia, 999',
                           'cidade': 'Tamboreu do Sul',
                           'estado': 'MG',
                           'cep': 44454058
                       },
    'telefone': [
                            {
                                'tipo': 'fixo',
                                'numero': '616 555-1234'
                            },
                            {
                                'tipo': 'celular',
                                'numero': '(55)(11)9.5599-8899'
                            }
                     ]
}
]
