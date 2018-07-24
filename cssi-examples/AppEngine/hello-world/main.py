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
        name = self.request.get("name")
        location = self.request.get("location")
        template = env.get_template("templates/hello.html")
        templateVars = {
            "name": name,
            "location": location,
        }
        self.response.write(template.render(templateVars))

class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("Shhh, this is a secret!")

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

class Students(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/students.html")
        templateVars = {
            "location": "MTV",
            "students": ["Kidus", "Leo", "Phoebe", "Jenny", "Lily", "Elvin"]
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/secret", SecretEntrance),
    ("/home", Home),
    ("/activities", Activities),
    ("/students", Students),
    ("/images", Images),
    ("/links", Links),
], debug=True)
