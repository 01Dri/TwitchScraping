
class Scrapper:

    def __init__(self, driver,by) -> None:
        self.driver = driver
        self.by = by
        self.title = None
        self.views = None
        self.game = None
        self.status = None
        pass

    def parse_with_selenium(self):
        try:
            self.title = self.driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/h2').text
            self.views = self.driver.find_element(self.by.XPATH,'//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/p').text
            self.game = self.driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/a/span').text
            self.status = self.driver.find_element(self.by.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[1]/div/div/div/a/div[2]/div/div/div/div/p').text
            return {'title':self.title, 'views':self.views, 'game':self.game, 'status':self.status}
        except Exception as e:
            print(e)
            return {'title':self.title, 'views':self.views, 'game':self.game, 'status':self.status}