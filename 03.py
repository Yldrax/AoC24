"""
    December 03, 2024

"""

from re import findall

"""
    Part 01
"""

def multiplication_sum(string1: str) -> int:
    mult_sum = 0

    # Finding the "mul(xxx,yyy) patterns
    matches = findall(r"mul\(\d{1,3},\d{1,3}\)", string1)
    # Extracting the numbers
    matches = [findall(r"\d{1,3}", _match) for _match in matches]
    # Converting to integers
    matches = [[int(_x) for _x in _match] for _match in matches]
    # Multiplying and adding
    mult_sum = sum(_x * _y for _x, _y in matches)

    return mult_sum

"""
    Part 02
"""

def multiplication_sum_conditional(string1):
    mult_sum = 0

    # Finding the "mul(xxx,yyy)", "do" or "don't" patterns
    matches = findall(r"mul\(\d{1,3},\d{1,3}\)|don't|do", string1)
    # extracting only the relevant numbers"
    matches_do = []
    dont = False
    for match in matches:
        if match == "do":
            dont = False
        elif match == "don't":
            dont = True
        elif not dont:
            matches_do.append(match)

    # Extracting the numbers
    matches_do = [findall(r"\d{1,3}", _match) for _match in matches_do]
    # Converting to integers
    matches_do = [[int(_x) for _x in _match] for _match in matches_do]
    # Multiplying and adding
    mult_sum = sum(_x * _y for _x, _y in matches_do)

    return mult_sum

"""
    Using the Functions
"""

if __name__ == '__main__':

    # Getting the String and removing the newlines
    file = open('inputs/03.txt', 'r')
    input_str = file.read()
    file.close()
    input_str = input_str.replace("\n","")

    # Applying the functions
    print(f"The sum of all Multiplications is: {multiplication_sum(input_str)}")
    print(f"The sum of all Multiplications where do is present is: {multiplication_sum_conditional(input_str)}")