from flask import Flask
import random
app = Flask(__name__)

facts_list = ['''Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.''','''Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.''',
              '''Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.''']

coin_list =['''Выпал ОРЁЛ''','''Выпала РЕШКА''']

@app.route("/")
def home():
    return f' <h1 style="display:flex; justify-content: center;  ">Главная страница</h1> <a href="/random_fact" style="text-decoration:none;color:black;display:flex; justify-content: center;">Посмотреть случайный факт!</a> <div style="display:flex; justify-content: center;"> <a href="/coin" style="text-decoration:none;color:black;"> <figure style="margin-left: 0px; margin-right: 0px;"> <img src="https://img.freepik.com/free-vector/golden-coin-with-clover-icon_18591-82408.jpg?semt=ais_hybrid&amp;w=740" style=width:118px;> <figcaption>Бросить монетку</figcaption> </figure> </a> </div>'
    
@app.route("/random_fact")
def fact():
    return f'<p>{random.choice(facts_list)}</p> '

@app.route("/coin")
def coin():
    return f'<p>{random.choice(coin_list)}</p> '




app.run(debug=True)

