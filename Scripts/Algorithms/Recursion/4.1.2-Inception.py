def inception(counter = 0):
    if counter > 3:
        return "Done!"
    return inception(counter + 1)

print(inception())

# 1. Identify the base case
# 2. Identify the recursive case
# 3. Get closer and closer and return when neede