# The Story
# Once a upon time, there was a classroom where
# a bunch of students went to ***Google*** and learned
# Computer Science with Googlers. These students
# ate a bunch of ***food*** everyday and learned things
# like ***HTML***, ***CSS***, and ***JavaScript***. They had
# a lot of ***fun*** and hope to work back at Google
# one day. The end.

name = input("Name a name: ")
company = input("Name a company: ")
topic = input("Name a topic you can learn: ")
people = input("Name a noun: ")
food = input("Name a food: ")
language1 = input("Name a language: ")
language2 = input("Name another language: ")
sport = input("Name a sport: ")
noun = input("Name a noun: ")

print(
    """
        Once a upon time, there was a classroom where a bunch of
        students went to %s and learned %s with %s. These students
        ate a bunch of %s everyday and learned things
        like %s, %s, and %s. %s had a lot of %s and hope to work
        back at %s one day. The end.
    """ % (company, topic, people, food, language1, language2, sport, name, noun, company)
)
