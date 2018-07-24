#main.py
#the import section

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Email(object):
    def __init__(self, subject, sender, content):
        self.subject = subject
        self.sender = sender
        self.content = content

emails = {
    Email("Test", "ciera@google.com", "This is a test email"),
    Email("Test2", "ciera@google.com", "This is the second email"),
    Email("Other Test", "ciera@google.com", "Final test email"),
}
# make it a link to ur email with slash email page -> make a link here + modify main.py and don't sha
#the handler section
class ListEmails(webapp2.RequestHandler):
    def get(self): #for a GET request
        template = env.get_template("templates/listemails.html")
        templateVars = {
            "emails": emails,
        }
        self.response.write(template.render(templateVars))

class ViewEmails(webapp2.RequestHandler):
    def get(self): #for a GET request
        # Creating variables to change the values of templateVars through URL finessing 
        subject = self.request.get("subject")
        sender = self.request.get("sender")
        content = self.request.get("content")
        template = env.get_template("templates/viewemails.html")
        templateVars = {
            "subject": subject,
            "sender": sender,
            "content": content,
        }
        self.response.write(template.render(templateVars))


#the app configuration section
app = webapp2.WSGIApplication([
    ("/", ListEmails), #this maps the root url to the MainPage Handler
    ("/emails", ViewEmails),
], debug=True)
