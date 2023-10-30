
import json
import logging

class Scrapper:

    def __init__(self, webdriver,by, streamer) -> None:
        self.webdriver = webdriver
        self.by = by
        self.url = f"https://www.twitch.tv/{streamer}"
        pass

    def parse_with_selenium(self):
        options = self.webdriver.EdgeOptions()
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = self.webdriver.Edge(options=options)
        driver.get(self.url)
        try:

            title = driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/h2').text
            views = driver.find_element(self.by.XPATH,'//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/p').text
            game = driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/a/span').text
            status = driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[1]/div/div/div/a/div[2]/div/div/div/div/p').text
            driver.quit()

            return {'title':title, 'views':views, 'game':game, 'status':status}
        except:
            return {'title':None, 'views':None, 'game':None, 'status':None}

