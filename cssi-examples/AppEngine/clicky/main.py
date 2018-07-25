import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

# Makes clicks a single instance where everyone can update it
class ClickCounter(ndb.Model):
    clicks = ndb.IntegerProperty()

# Handlers
class MainPage(webapp2.RequestHandler):
    def get(self):
        # Load the click counter from the database
        click_counter = ClickCounter.query().get()

        # Check in case this is the first click + makes a new ClickCounter object
        if not click_counter:
            click_counter = ClickCounter(clicks=0)
        templateVars = {
            "click_count": click_counter.clicks,
        }
        template = env.get_template("templates/clicky.html")
        self.response.write(template.render(templateVars))

    def post(self):
        # Load the click counter from the database
        click_counter = ClickCounter.query().get()

        # Check in case this is the first click + makes a new ClickCounter object
        if not click_counter:
            click_counter = ClickCounter(clicks=0)

        click_counter.clicks += 1
        # Writes the updated value into the database
        click_counter.put()
        templateVars = {
            "click_count": click_counter.clicks,
        }
        template = env.get_template("templates/clicky.html")
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
