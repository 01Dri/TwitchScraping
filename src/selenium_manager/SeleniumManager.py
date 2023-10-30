class SeleniumManager:

    def __init__(self, url, webdriver) -> None:
        self.driver_edge = webdriver
        self.url = url
        pass

    def get_webdriver(self):
        options = self.driver_edge.EdgeOptions()
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver_edge = self.driver_edge.Edge(options=options)
        return self.driver_edge

    def get_browser(self):
        self.driver_edge.get(self.url)
        return self.driver_edge
    
    def close_browser(self):
        self.driver_edge.quit()




