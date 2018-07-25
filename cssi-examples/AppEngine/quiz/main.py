# main.py
# the import section

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class CollectInfo(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/quiz.html")
        self.response.write(template.render())

class Submitted(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("templates/submit.html")
        food = self.request.get("food")

        if food == "Sushi":
            image = "https://i.ytimg.com/vi/2CgONJkdnS0/maxresdefault.jpg"
            type = "water"
        elif food == "Burger":
            image = "https://i1.wp.com/ungroovygords.com/wp-content/uploads/2016/06/picture2life_79607_original1.jpg?fit=720%2C720&ssl=1"
            type = "normal"
        elif food == "Pasta":
            image = "https://img00.deviantart.net/260b/i/2011/352/e/3/electric_pokemon__wallpaper_by_55darkabyss-d4jius3.jpg"
            type = "electric"
        elif food == "Pad Thai":
            image = "https://78.media.tumblr.com/791564b8e9ea3ee7155c1ffee5d31f45/tumblr_inline_mscj7zmY6w1qz4rgp.png"
            type = "ground"

        templateVars = {
            "food": food,
            "image": image,
            "type": type
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", CollectInfo),
    ("/submitted", Submitted),
], debug=True)
