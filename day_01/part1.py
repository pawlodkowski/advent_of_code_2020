"""
Find the two entries (from input.txt) that sum to 2020; 
what do you get if you multiply them together?
"""
TARGET = 2020

with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [int(num) for num in data]
# wonder if there's a way to do this upon reading

for num in data:
    complement = TARGET - num
    if complement in data:
        first = num
        second = complement
        break

assert first + second == TARGET

print(
    f"Solution: {first} and {second} add to {TARGET} and their product is {first*second}"
)
