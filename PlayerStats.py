import requests
from requests import get
from requests import post

import os
import json
from time import sleep

from datetime import datetime

def cls():
    os.system('cls||clear')

def stat():
    nickname = input(" Введите никнейм игрока: ")
    data = {
        "search": nickname,
        "type": "exact"
    }
    stat_request = post("https://api.worldoftanks.ru/wot/account/list/?application_id=a022362c5057adcfa80ed59cbd284584", params=data)
    count = stat_request.json()['meta']['count']
    if count == 1:
        id = stat_request.json()['data'][0]['account_id']
        id_data = {
            "account_id": id
        }

    if count == 1:
        print(" Аккаунт найден!")
        print(" ID Аккаунта: " + str(id))
        print(" Выполняю полный поиск по ID...")
        print("")
        sleep(2)
        while True:
            all_stat_request = post("https://api.worldoftanks.ru/wot/account/info/?application_id=a022362c5057adcfa80ed59cbd284584", params=id_data)

            created_timestamp = all_stat_request.json()['data'][str(id)]['created_at']
            created_data = datetime.utcfromtimestamp(created_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print(" Аккаунт создан: " + str(created_data))
            
            global_rating = all_stat_request.json()['data'][str(id)]['global_rating']           
            print(" Глобальный рейтинг: " + str(global_rating))

            battles = all_stat_request.json()['data'][str(id)]['statistics']['all']['battles']
            print(" Всего боёв проведено: " + str(battles))

            print("")

            wins = all_stat_request.json()['data'][str(id)]['statistics']['all']['wins']            
            print(" Побед: " + str(wins))

            losses = all_stat_request.json()['data'][str(id)]['statistics']['all']['losses']
            print(" Поражений: " + str(losses))

            draws = all_stat_request.json()['data'][str(id)]['statistics']['all']['draws']
            print(" Ничьей: " + str(draws))


            print("")

            spotted = all_stat_request.json()['data'][str(id)]['statistics']['all']['spotted']
            print(" Всего противников обнаружено: " + str(spotted))
            
            frags = all_stat_request.json()['data'][str(id)]['statistics']['all']['frags']
            print(" Всего техники уничтожено: " + str(frags))

            trees_cut = all_stat_request.json()['data'][str(id)]['statistics']['trees_cut']
            print(" Всего деревьев повалено: " + str(trees_cut))

            print("")

            print(" Информация обновляется раз в 5 минут")
            break_loop = input(" Нажмите Enter для остановки обновления информации и возврата в меню: ")
            if break_loop == "":
                cls()
                menu()
                break
            else:   
                cls()
                menu()     
            sleep(300)
            cls()

    else:
        print( "Ошибка")

def menu():
    stat_start = input(" Введите 1 для получения статистики игрока: ")
    if stat_start == "1":
        cls()
        stat()
    else:
        print(" Ошибка! ")

def connect():
    status = get("https://api.worldoftanks.ru/wot/account/list/?application_id=a022362c5057adcfa80ed59cbd284584")
    if status.status_code == 200:
        print(" Подключение к API успешно...")
        print("")
        menu_start = input(" Для входа в меню введите 1: ")
        if menu_start == "1":
            cls()
            menu()
        else:
            print(" Ошибка! ")
    else:
        print(" Ошибка подключения!")
    
print(" Запуск...")
connect()