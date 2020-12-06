"""
UPDATED POLICY:
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

How many passwords are valid according to the new interpretation of the policies?
"""

import re
import operator


def is_valid(policy: str, password: str) -> bool:
    """
    Given a policy (e.g. `1-3 a`) and a password (e.g. `abcde`),
    determine if the password complies with the policy
    """
    char = policy[-1:]
    pos_1 = int(re.findall("[0-9]+", policy)[0])
    pos_2 = int(re.findall("[0-9]+", policy)[1])

    return operator.xor((password[pos_1 - 1] == char), (password[pos_2 - 1] == char))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().split("\n")

    val_pwds = 0
    for i in data:
        pol = i.split(":")[0].strip()
        pwd = i.split(":")[1].strip()
        if is_valid(pol, pwd):
            val_pwds += 1

    print(f"Solution: {val_pwds} valid passwords out of {len(data)}")
