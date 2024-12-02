import numpy as np

"""
    December 1
"""

"""
    Part 01
"""

file01 = open('input_01_01.txt', 'r')
input01 = file01.read()
file01.close()

input01 = input01.replace("\n","   ").strip().split("   ")

input01_01 = []
input01_02 = []

for k in range(0,len(input01), 2):
    input01_01.append(int(input01[k]))
    input01_02.append(int(input01[k+1]))

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
    Use the Functions
"""

if __name__ == '__main__':
    print(f"The Distance is {list_compare(input01_01, input01_02)}!")
    print(f"The Similarity is {list_similarity(input01_01, input01_02)}!")


