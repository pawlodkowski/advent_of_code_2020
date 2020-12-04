"""
Count the number of valid passports - those that have all required fields.
Treat cid as optional.
In your batch file, how many passports are valid?
"""


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read()
    data = data.split("\n\n")
    return data


if __name__ == "__main__":
    valid_entries = 0
    data = read_data("input.txt")
    for entry in data:
        if "cid" not in entry:
            if entry.count(":") <= 6:
                pass
            else:
                valid_entries += 1
        else:
            if entry.count(":") < 8:
                pass
            else:
                valid_entries += 1

    print(f"Solution: {valid_entries} valid passports found.")
