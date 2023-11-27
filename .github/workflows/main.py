import requests as server
#from flask import Flask
from random import randint
from time import sleep

# Dados
firebaseurl = "https://animedungeons-rblx-default-rtdb.firebaseio.com/"
token = ''

url = f"{firebaseurl}.json?auth={token}"

# Heróis do banner
heroes = {
    'common': [
        'Naruto', 'Goku'
    ],

    'uncommon': [
        'SrDinnin'
    ],

    'rare': [
        'iun'
    ],

    'legendary': [
        'Meu pau lendário'
    ],
}


def heroisaleatorios():
    escolhidos = {'common': 0, 'common2': 0, 'common3': 0, 'uncommon': 0, 'rare': 0, 'legendary': 0}

    escolhidos['common'] = heroes['common'][randint(0, len(heroes['common'])-1)]
    escolhidos['common2'] = heroes['common'][randint(0, len(heroes['common'])-1)]
    escolhidos['common3'] = heroes['common'][randint(0, len(heroes['common'])-1)]
    escolhidos['uncommon'] = heroes['uncommon'][randint(0, len(heroes['uncommon'])-1)]
    escolhidos['rare'] = heroes['rare'][randint(0, len(heroes['rare'])-1)]
    escolhidos['legendary'] = heroes['legendary'][randint(0, len(heroes['legendary'])-1)]
    return escolhidos

def aplicar():
    print('Adicionando os novos heróis ao banner...')
    dados = heroisaleatorios()

    response = server.put(url, json=dados)
    if response.status_code == 200:
        print('Os novos heróis foram adicionados.')

def apagardados():
    print('Apagando os heróis do banner...')
    response = server.delete(url)
    if response.status_code == 200:
        print("Todos os heróis do banner foram apagados com sucesso.")


#app = Flask('__main__')
#@app.route('/atualizar-firebase', methods=['POST'])

def atualizar_firebase():
    apagardados()
    sleep(1)
    aplicar()
    #return 'Operação concluída com sucesso!', 200


#app.run(debug=True, port=5000)
