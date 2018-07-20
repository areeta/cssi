states = {
    "CA" : "California",
    "AZ" : "Arizona",
    "AK" : "Arkansas"
}

for state in states:
    print("%s is the abbreviation for %s" % (state, states[state]))

store_prices = {
    "cereal" : 2.00,
    "stapler" : 1.50,
    "fiber optic" : 25,
    "lambo": 750000,
}

print(store_prices["cereal"] + store_prices["lambo"])
