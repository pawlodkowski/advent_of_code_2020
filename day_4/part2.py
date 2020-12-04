"""
Count the number of valid passports - those that have all required fields and valid values.
Continue to treat cid as optional. In your batch file, how many passports are valid?
"""

from part1 import read_data
import re


def extract_field_val(field: str, entry) -> str:
    return re.findall(f"{field}:([^\s]+)", entry)[0]


def get_validity_errors(field_vals: dict) -> list:

    if "cm" in field_vals["hgt"]:
        hgt_cond = 150 <= int(field_vals["hgt_val"]) <= 193
    elif "in" in field_vals["hgt"]:
        hgt_cond = 59 <= int(field_vals["hgt_val"]) <= 76
    else:
        hgt_cond = False

    errors = [
        reason
        for (invalid, reason) in (
            (
                not (len(field_vals["byr"]) == 4)
                & (1920 <= int(field_vals["byr"]) <= 2002),
                "Birth Year Invalid",
            ),
            (
                not (len(field_vals["iyr"]) == 4)
                & (2010 <= int(field_vals["iyr"]) <= 2020),
                "Issue Year Invalid",
            ),
            (
                not (len(field_vals["eyr"]) == 4)
                & (2020 <= int(field_vals["eyr"]) <= 2030),
                "Exp. Year Invalid",
            ),
            (not hgt_cond, "Height Invalid"),
            (not len(field_vals["hex_color"][1:]) == 6, "Hair Color Invalid"),
            (
                not field_vals["ecl"]
                in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                "Eye Color Invalid",
            ),
            (not len(field_vals["pid_val"]) == 9, "Passport ID Invalid"),
        )
        if invalid
    ]

    return errors


def is_valid_pass(entry: str) -> bool:

    entry = entry.replace("\n", " ")
    field_vals = {
        "byr": None,
        "iyr": None,
        "eyr": None,
        "hgt": None,
        "hcl": None,
        "ecl": None,
        "pid": None,
    }

    try:
        for f in field_vals:
            field_vals[f] = extract_field_val(f, entry)

        field_vals["hgt_val"] = re.findall("[0-9]+", field_vals["hgt"])[0]
        field_vals["hex_color"] = re.findall("#[a-f0-9]+", field_vals["hcl"])[0]
        field_vals["pid_val"] = re.findall("[0-9]+", field_vals["pid"])[0]

        errors = get_validity_errors(field_vals)

    except IndexError:
        return False

    if not errors:
        return True

    return False


if __name__ == "__main__":
    valids = 0
    data = read_data("input.txt")
    for i in data:
        if is_valid_pass(i):
            valids += 1
    print(f"Solution: {valids} valid passwords based on new rules")
