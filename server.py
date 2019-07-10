import tornado.web
import tornado.ioloop
import tornado.httpclient
import json

class HelloWorld(tornado.web.RequestHandler):
  async def get(self):
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = await http_client.fetch("https://node-api.jess.gallery/v1/slider_images")
    slides = response.body.decode('utf-8')
    self.render("main.html", slides=json.loads(slides))

def main():
  app = tornado.web.Application([
    ("/", HelloWorld)
  ], debug=True, template_path="templates", static_path="static")
  app.listen(8888)
  print("app is listening at http://localhost:8888")
  tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
  main()
