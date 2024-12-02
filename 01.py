"""
    December 01, 2024

"""

"""
    Part 01
"""

def list_compare(list1: list[int], list2: list[int]) -> int:
    sorted1 = list1
    sorted2 = list2
    distance = 0
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        distance += abs(sorted1[i] - sorted2[i])

    return distance

"""
    Part 02
"""

def list_similarity(list1: list[int], list2: list[int]) -> int:
    num_dict = {}
    similarity = 0

    for number in list2:
        if number in num_dict:
            num_dict[number] += 1
        else:
            num_dict[number] = 1

    for number in list1:
        if number in num_dict:
            similarity += number * num_dict[number]

    return similarity

"""
    Using the Functions
"""

if __name__ == '__main__':

    # Getting the String and splitting it into a list
    file = open('inputs/01.txt', 'r')
    input_str = file.read()
    file.close()

    input_list = input_str.replace("\n", "   ").strip().split("   ")

    input1 = []
    input2 = []

    # Splitting the list
    for k in range(0, len(input_list), 2):
        input1.append(int(input_list[k]))
        input2.append(int(input_list[k + 1]))

    # Actually applying the functions
    print(f"The Distance is {list_compare(input1, input2)}!")
    print(f"The Similarity is {list_similarity(input1, input2)}!")


