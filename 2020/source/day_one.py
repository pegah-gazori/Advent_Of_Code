"""Solution For Day One"""


PROBLEM_URL = "https://adventofcode.com/2020/day/1"


def parse_data(data_path):
    """Parsing data from text file."""

    data = open(data_path, "r").read().split("\n")
    return list(map(int, data))


def find_number_pair(sum_value, data):
    """Finding the two entries that sum to sum_value. Final result is the multiply of those entries."""

    for first_index, first_value in enumerate(data):
        for second_index, second_value in enumerate(data):
            if first_index != second_index:
                if first_value + second_value == sum_value:  # OR if second_value == sum_value - first_value:
                    print(f"Sum is {sum_value}!")
                    return first_value * second_value


if __name__ == '__main__':
    parsed_data = parse_data(data_path="../data/day_one_data.txt")
    result = find_number_pair(sum_value=2020, data=parsed_data)
    print(f"Multiply Is {result}")
