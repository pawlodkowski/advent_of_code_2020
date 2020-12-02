"""
Added complexity:
Find the THREE entries (from input.txt) that sum to 2020; 
what do you get if you multiply them together?

Not the most scalable solution, but it works :)
"""


with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [int(num) for num in data]
# wonder if there's a way to do this upon reading

target = 2020
for i in data:
    new_target = target - i  # would be the sum of the other 2 unknown numbers
    for j in data:
        complement = new_target - j
        if complement in data:
            first = i
            second = j
            third = complement
            break

assert first + second + third == target

print(
    f"Solution: {first} and {second} and {third} add to {target} and their product is {first*second*third}"
)