# Using states to learn libraries
states = {
    "CA" : "California",
    "AZ" : "Arizona",
    "AK" : "Arkansas"
}

for state in states:
    print("%s is the abbreviation for %s" % (state, states[state]))

# Creating a store with prices
store_prices = {
    "cereal" : 2.00,
    "stapler" : 1.50,
    "fiber optic" : 25,
    "lambo": 750000,
}
# Finding 2 times (store price of cereal plus store price of the lambo
print(2 * store_prices["cereal"] + store_prices["lambo"])

# Creating a store with amount of invetory
store_inventory = {
    "cereal" : 3,
    "stapler" : 6,
    "fiber optic" : 2,
    "lambo": 75,
}

# Minus 2 lambos and cereals from inventory
store_inventory["lambo"] -= 2
store_inventory["cereal"] -=2

# Jack up the price from all store items from 3%
for price in store_prices:
    store_prices[price] *= 1.03

print(store_prices)
