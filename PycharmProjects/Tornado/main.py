import tornado.ioloop
import tornado.web

Asia_nickname = "levik"
Europe_nickname = "Ustycmd"
America_nickname = "BruTo"




class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        region = self.get_argument('region', None)
        if region == "Asia":
            self.write({'ab':"Top 1 {Asia_nickname}, {region}".format(Asia_nickname=Asia_nickname, region=region)})
        elif region == "Europe":
            self.write({'ab':"Top 1 {Europe_nickname}, {region}".format(Europe_nickname=Europe_nickname, region=region)})
        elif region == "America":
            self.write({'ab':"Top 1 {America_nickname}, {region}".format(America_nickname=America_nickname, region=region)})
        else:
            return self.write("You write incorrect region")




def make_app():
    return tornado.web.Application([
        (r"/", RequestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()