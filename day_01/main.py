import os
import re
import sys

words_to_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def number_as_digit_string(n_str):
    try:
        return str(int(n_str))
    except:
        return words_to_numbers[n_str]

def main():

    calibration_numbers = []

    # arg[1]: input file to use
    # arg[2]: part of the daily challenge to run

    with open(sys.argv[1]) as file:

        for line in file.readlines():

            matches = None
            if sys.argv[2] == '1':
                # For first part
                matches = re.findall(".*?(\\d)", line)
             
            elif sys.argv[2] == '2':
                # For second part
                matches = [
                    re.findall(".*?((?:zero)|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)|\\d)", line)[0],
                    re.findall(".*((?:zero)|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)|\\d)", line)[0]
                ]            

            calibration_numbers.append(
                int(
                    "".join([
                        number_as_digit_string(matches[0]),
                        number_as_digit_string(matches[len(matches) - 1])
                    ])
                )
            )

    return sum(calibration_numbers)

if __name__ == "__main__":
    print(main())

