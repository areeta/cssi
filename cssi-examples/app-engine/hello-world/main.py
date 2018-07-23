import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1>Hello, World!</h1>")
        self.response.write("<i>Hello, World! We have learned about:</i>")
        self.response.write("<ul></ul>")
        self.response.write("<li>HTML</li>")
        self.response.write("<li>CSS</li>")
        self.response.write("<li>Javascript</li>")
        self.response.write("<li>Python</li>")
        self.response.write("<li>Command Line</li>")
        self.response.write("<li>GitHub</li>")
        self.response.write("<li>AppEngine</li>")
        self.response.write("<ul></ul>")
        self.response.write("<a href='/bye'>Goodbye</a>")

class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("Shhh, this is a secret!")

class GoodBye(webapp2.RequestHandler):
    def get(self):
        self.response.write("Bye Bye!")

class About(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello! This is YAMLLLLLLLLL!")

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/secret", SecretEntrance),
    ("/bye", GoodBye),
    ("/about", About),

], debug=True)
