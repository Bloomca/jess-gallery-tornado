import tornado.web
import tornado.ioloop

class HelloWorld(tornado.web.RequestHandler):
  def get(self):
    self.render("hello.html")

def main():
  app = tornado.web.Application([
    ("/", HelloWorld)
  ], debug=True, template_path="templates")
  app.listen(8888)
  print("app is listening at http://localhost:8888")
  tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
  main()
