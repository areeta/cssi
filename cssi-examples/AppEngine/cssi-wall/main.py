import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)

class Message(ndb.Model):
    name = ndb.StringProperty()
    content = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class Wall(webapp2.RequestHandler):
    def get(self):
    # Common Things to Do with a Handler

        # 1. Get info from the user request
            # We don't need to here

        # 2. Read from (WE DID THIS) or write to the database
        messages = Message.query().order(-Message.created_time).fetch()

        # 3. Render a response back to user or computer
        templatesVar = {
            "messages": messages,
        }
        template = env.get_template("templates/wall.html")
        self.response.write(template.render(templatesVar))

    def post(self):
    # Common Things to Do with a Handler

        # 1. Get info from the user request
        name = self.request.get("name")
        content = self.request.get("content")

        # 2. Read from or write (WE DID THIS) to the database
        newMessage = Message(name=name, content=content)
        newMessage.put()

        # 3. Render a response back (OR RELOAD TO SOMEWHERE ELSE) to user or computer
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/", Wall),
], debug=True)
