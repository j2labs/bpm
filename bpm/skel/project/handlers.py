from brubeck.request_handling import WebMessageHandler

class TakeFiveHandler(WebMessageHandler):
    def get(self):
        name = self.get_argument('name', 'dude')
        self.set_body('Take five, %s!' % name)
        return self.render()
