#main.py
#the import section

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Email(object):
    def __init__(self, subject, sender, content, image):
        self.subject = subject
        self.sender = sender
        self.content = content
        self.image = image

emails = {
    Email("Cats are cute", "ciera@google.com", "Meow Meow", "https://i2-prod.mirror.co.uk/incoming/article11238103.ece/ALTERNATES/s1200/PAY-KITTENS-CUDDLING.jpg"),
    Email("I love cats", "ciera@google.com", "cattos lattos battos", "http://cdn.earthporm.com/wp-content/uploads/2015/07/sleeping-kitties-1__6051.jpg"),
    Email("Cute cats for sale", "ciera@google.com", "Meoooowowowowowowowowowowwwowo", "https://www.petmd.com/sites/default/files/petmd-kitten-facts.jpg"),
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
        image = self.request.get("image")
        template = env.get_template("templates/viewemails.html")
        templateVars = {
            "subject": subject,
            "sender": sender,
            "content": content,
            "image": image,
        }
        self.response.write(template.render(templateVars))


#the app configuration section
app = webapp2.WSGIApplication([
    ("/", ListEmails), #this maps the root url to the MainPage Handler
    ("/emails", ViewEmails),
], debug=True)
