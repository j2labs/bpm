from brubeck.request_handling import WebMessageHandler, JSONBaseHandler


class LandingHandler(WebMessageHandler):
    def get(self):
        name = self.get_argument('name', 'dude')
        self.set_body('Take five, %s!' % name)
        return self.render()


class APILandingHandler(JSONBaseHandler):
    def get(self):
        self.add_to_payload('data', {'hello': 'would you like to play a game?'})
        return self.render(status_code=200)
