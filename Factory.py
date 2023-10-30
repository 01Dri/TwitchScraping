from Streamer import Streamer
class Factory:

    def __init__(self, parser) -> None:
        self.parser = parser
        pass
    
    def get_streamer(self):
        title = self.parser['title']
        views = self.parser['views']
        game = self.parser['game']
        status = self.parser['status']
        if (status == None):
            return Streamer(title, views, game, "Offiline")
        return Streamer(title, views, game, status)
        

