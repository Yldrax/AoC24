"""
    December 05, 2024

"""

"""
    Part 01
"""

def order_updates():
    pass

def sum_middles(list1) -> int:
    middle_sum = 0
    for i in range(len(list1)):
        middle_sum += list1[i][len(list1[i]) // 2]
    return middle_sum


"""
    Part 02
"""

def placeholder2():
    pass

"""
    Using the Functions
"""

if __name__ == '__main__':

    # Getting the String and splitting it into a list
    file = open('inputs/05.txt', 'r')
    input_str = file.read()
    file.close()

    # Split the Lists
    rules_str, updates_str = input_str.split("\n\n")
    rules_list = rules_str.strip().split("\n")
    updates_list = updates_str.strip().split("\n")

    # Convert the rules into tuples
    for k in range(len(rules_list)):
        rules_list[k] = rules_list[k].split("|")
        rules_list[k] = tuple(int(x) for x in rules_list[k])

    # Convert the updates into lists
    for k in range(len(updates_list)):
        updates_list[k] = [int(x) for x in updates_list[k].split(",")]

    print(rules_list)
    print(updates_list)