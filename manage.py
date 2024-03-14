from flask import Flask, render_template


class Serie:
    def __init__(self,lista, foto, nome, legenda):
        self.lista = lista
        self.foto = foto
        self.nome = nome
        self.legenda = legenda

app = Flask(__name__)

from link import *
from queens import *
from secretaria_kim import *
from herdeiro import *
from frieren import *

@app.route('/')
def index():
    serie1 = Serie('lista','../static/assets/imagens/link_me.jpeg', 'Conexão: Comer, Amar e Matar', '2022 ‧ Romance ‧ 1 temporada')
    serie2 = Serie('lista2','../static/assets/imagens/queen.jpeg', 'Queen of Tears', '2024 ‧ Drama ‧ 1 temporada')
    serie3 = Serie('lista3','../static/assets/imagens/secret_kim_capa.jpeg','O que há de errado com a secretária Kim?', '2018 ‧ Romance ‧ 1 temporada')
    serie4 = Serie('lista_herdeiro','../static/assets/imagens/herdeiro.jpeg', 'O Herdeiro Impossível', '2024 ‧ Drama ‧ 1 temporada')
    serie5 = Serie('lista_frieren', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT6ytG9Q53tUhhMw7b1FiwjxD6lMg8a6COFUNxnCrKnizwKLvP6',"Frieren: Beyond Journey's End",'2023 ‧ 1 temporada')
    lista = [serie1, serie2, serie3, serie4,serie5]
    return render_template('index.html', series=lista)

@app.route('/lista')
def lista():
    return render_template ('listas/lista.html')

@app.route('/lista2')
def lista2():
    return render_template ('listas/lista2.html')

@app.route('/lista3')
def lista3():
    return render_template ('listas/lista3.html')

@app.route('/lista_herdeiro')
def lista_herdeiro():
    return render_template('listas/lista_herdeiro.html')

@app.route('/lista_frieren')
def lista_frieren():
    return render_template('listas/lista_frieren.html')


app.run(debug=True)