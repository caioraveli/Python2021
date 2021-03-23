perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '6',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*3? ',
        'respostas': {
            'a': '6',
            'b': '0',
            'c': '3',
            'd': '9',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quem descobriu o Brasil? Pedro Alvares Ca.. ',
        'respostas': {
            'a': 'bral',
            'b': 'brel',
            'c': 'bril',
            'd': 'brol',
            'e': 'brul',
        },
        'resposta_certa': 'a',
    },
}

for pk,pv in perguntas.items():
    print(f'{pk}: ')
    print(pv['pergunta'])
    for rk,rv in pv['respostas'].items():
        print(f'{rk}: {rv}')
    res = input('Digite sua resposta: ')

    if  res not in ('a','b','c','d','e'):
        print('Voce precisa digitar uma letra: a,b,c,d,e..')
        continue
    if res == pv['resposta_certa']:
        print('Certa resposta!!!')
    else:
        print(f"Errou!! Resposta correta: {pv['resposta_certa']}")

    print()
