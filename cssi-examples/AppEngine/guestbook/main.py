import webapp2
import jinja2
import os
import logging
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)

class Message(ndb.Model):
    email = ndb.StringProperty()
    content = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        login_url = ""
        logout_url = ""
        # 1. Get information from the request => The current user will be a user object or None.
        current_user = users.get_current_user()

        # If no one is logged in, show a login prompt.
        if not current_user:
            login_url = users.create_login_url("/")
        else:
            logout_url = users.create_logout_url("/")

        # 2. Read/write from the database.
        messages = Message.query().order(-Message.created_time).fetch()

        templateVars = {
            "current_user": current_user,
            "login_url": login_url,
            "logout_url": logout_url,
            "messages": messages,
        }

        template = env.get_template("/templates/guestbook.html")
        self.response.write(template.render(templateVars))

    def post(self):
        # 1. Get information from the request
        email = users.get_current_user().email()
        content = self.request.get("content")
        # 2. Read/write to the database
        message = Message(email=email, content=content)
        message.put()
        # 3. Render a response -> let the user see their message on the same page
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
