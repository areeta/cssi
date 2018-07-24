# 1. Import jinja in app.yaml
# 2. Import jinja + os in main.py
# 3. Setup jinja environment
# 4. Get the template from the environment
# 5. Render the template

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/hello.html")
        self.response.write(template.render())

class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("Shhh, this is a secret!")

class GoodBye(webapp2.RequestHandler):
    def get(self):
        self.response.write("Bye Bye!")

class Home(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/home.html")
        self.response.write(template.render())

class Activities(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/activities.html")
        self.response.write(template.render())

class Images(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/images.html")
        self.response.write(template.render())

class Links(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/links.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/secret", SecretEntrance),
    ("/bye", GoodBye),
    ("/home", Home),
    ("/activities", Activities),
    ("/images", Images),
    ("/links", Links),
], debug=True)
