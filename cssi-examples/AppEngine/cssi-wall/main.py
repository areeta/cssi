import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)

# Handlers
class Message(ndb.Model):
    name = ndb.StringProperty()
    content = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class Wall(webapp2.RequestHandler):
    def get(self):
        message_query = Message.query().order(Message.created_time)
        messages = message_query.fetch()
        templatesVar = {
            "messages": messages,
        }
        template = env.get_template("templates/wall.html")
        self.response.write(template.render(templatesVar))
    def post(self):
        name = self.request.get("name")
        content = self.request.get("content")
        newMessage = Message(name=name, content=content)
        newMessage.put()
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/", Wall),
], debug=True)
