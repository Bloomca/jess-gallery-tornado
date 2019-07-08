import tornado.web
import tornado.ioloop

class HelloWorld(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world3!")

def main():
  app = tornado.web.Application([
    ("/", HelloWorld)
  ], debug=True)
  app.listen(8888)
  print("app is listening at http://localhost:8888")
  tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
  main()
