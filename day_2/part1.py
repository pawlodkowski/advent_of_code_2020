"""
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times
a given letter must appear for the password to be valid. 
For example, `1-3 a` means that the password must contain a at least 1
time and at most 3 times.

How many passwords are valid according to their policies?
"""

import re


def is_valid(policy: str, password: str) -> bool:
    """
    Given a policy (e.g. `1-3 a`) and a password (e.g. `abcde`),
    determine if the password complies with the policy
    """
    char = policy[-1:]
    atleast = int(re.findall("[0-9]+", policy)[0])
    atmost = int(re.findall("[0-9]+", policy)[1])
    assert atleast < atmost

    if atleast <= password.count(char) <= atmost:
        return True

    return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().split("\n")

    val_pwds = 0
    for i in data:
        pol = i.split(":")[0]
        pwd = i.split(":")[1]
        if is_valid(pol, pwd):
            val_pwds += 1

    print(f"Solution: {val_pwds} valid passwords out of {len(data)}")
