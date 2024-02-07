"""Solution For Day Two"""


PROBLEM_URL = "https://adventofcode.com/2020/day/2"


from aocd import get_data


def validate_password():

    total_number_of_valid_passwords = 0
    data = get_data(day=2, year=2020).split("\n")

    for row in data:
        elements = row.split()
        character_range = elements[0].split("-")
        minimum_character_count = int(character_range[0])
        maximum_character_count = int(character_range[1])
        character_to_count = elements[1].replace(":", "")
        password = elements[2]

        occurrences = int(password.count(character_to_count))
        if minimum_character_count <= occurrences <= maximum_character_count:
            total_number_of_valid_passwords += 1

    return total_number_of_valid_passwords


if __name__ == "__main__":
    print("Number of Valid Passwords: ", validate_password())