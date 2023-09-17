"""Solution For Day Two"""


PROBLEM_URL = "https://adventofcode.com/2020/day/2"


def parse_data(data_path):
    """Parsing data from a text file."""

    with open(data_path) as file:
        dict_data = {key: value for line in file for(key, value) in [line.strip().split(": ")]}
    return dict_data


def extracting_policy_elements(policy):
    """Extracting the elements of policy from the key of the data dictionary"""

    char_and_limit_split = policy.split(" ")
    limit_split = char_and_limit_split[0].split("-")

    min_char_num = int(limit_split[0])
    max_char_num = int(limit_split[1])
    char = char_and_limit_split[1]

    return min_char_num, max_char_num, char


def validate_password(input_data):
    """This function validates password based on their policies, and it returns the total number of valid passwords."""

    total_number_of_valid_password = 0

    for key, value in input_data.items():
        min_of_character, max_of_character, character_to_count = extracting_policy_elements(policy=key)
        occurrences = value.count(character_to_count)
        if min_of_character <= occurrences <= max_of_character:
            total_number_of_valid_password += 1

    return total_number_of_valid_password


if __name__ == "__main__":
    parsed_data = parse_data(data_path="../data/day_two_data.txt")
    number_of_valid_passwords = validate_password(input_data=parsed_data)
    print(f"Number of valid passwords: {number_of_valid_passwords}")
