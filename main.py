from Scrapper import Scrapper
from Factory import Factory
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
while True:


    print("STREAMER TÁ ON OU NÃO TÁ ?")
    name_search_streamer = input("DIGITE O NOME: ")
    scrapper = Scrapper(webdriver,By,name_search_streamer)
    streamer = Factory(scrapper.parse_with_selenium()).get_streamer()

    print(f'STREAMER: {name_search_streamer.upper()}')
    print("")
    print(f"STATUS: {streamer.status}")
    print(f"TITULO: {streamer.title}")
    print(f"JOGO: {streamer.game}")
    print(f"VIEWS: {streamer.views}")
    print("")
    input("APERTE ENTER")
    
    os.system('cls')



    