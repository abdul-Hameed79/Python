cars = ["BMW", "Mercedes", "TATA", "Tesla", "Mahindra"]
for i in cars:
    print(i)    #Output: BMW Mercedes TATA Tesla Mahindra
print("")


# using break statement
cars = ["BMW", "Mercedes", "TATA", "Tesla", "Mahindra"]
for x in cars:
    if x == "TATA":
        break
    print(x)    #Output: BMW Mercedes
print("")


# Using Continue statement
cars = ["BMW", "Mercedes", "TATA", "Tesla", "Mahindra"]
for y in cars:
    if y == "Mercedes":
        continue
    print(y)