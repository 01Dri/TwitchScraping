from scraper.Scrapper import Scrapper
from factory.Factory import Factory
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style, init
from selenium_manager.SeleniumManager import SeleniumManager
import os
import time

class Executor:

    def __init__(self, os) -> None:
        self.driver = SeleniumManager(None, webdriver)
        self.driver.get_webdriver()
        self.os = os
        pass
    def run(self):
        while True:
            self.os.system('cls')
            init(autoreset=True)
            print("""

 ____  _____ _____ ____  _____ _____ 
|    \| __  |     |    \|   __|  |  |
|  |  |    -|-   -|  |  |   __|  |  |
|____/|__|__|_____|____/|_____|\___/ 

""")
            print("STREAMER TÁ ON OU NÃO TÁ ?")
            name_search_streamer = ""
            while name_search_streamer == "":
                name_search_streamer = input("DIGITE O NOME: ").upper()
            URL = f"https://www.twitch.tv/{name_search_streamer}"
            self.driver.url = URL
            self.driver.get_browser()
            scrapper = Scrapper(self.driver.driver_edge,By)
            time.sleep(3)
            streamer = Factory(scrapper.parse_with_selenium()).get_streamer()
            os.system('cls')
            print(f'STREAMER: {Fore.BLUE}{name_search_streamer.upper()}')
            if streamer.status == 'AO VIVO':
                print(f"STATUS: {Fore.GREEN}{streamer.status}")
            else:
                print(f"STATUS: {Fore.RED}{streamer.status}")
            print(f"TITULO: {streamer.title}")
            print(f"JOGO: {streamer.game}")
            print(f"VIEWS: {streamer.views}")
            print("")
            choose = input("APERTE ENTER PARA CONTINUAR OU X PARA SAIR: ").lower()
            if choose == "x":
                self.driver.close_browser()
                break
            os.system('cls')

app = Executor(os)
app.run()



