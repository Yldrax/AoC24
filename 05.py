"""
    December 05, 2024

"""
from random import shuffle
"""
    Part 01
"""
def update_ordered(list1: list[int], dict1) -> bool:
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[j] in dict1:
                if list1[i] in dict1[list1[j]]: #check if list1[i] should be behind list1[j]
                    return False

    return True

def sum_ordered(list1: list[list[int]], dict1):
    ordered_sum = 0
    for update in list1:
        if update_ordered(update,dict1):
            ordered_sum += update[len(update) // 2]
    return ordered_sum

"""
    Part 02
"""
def order_update(list1: list[int], dict1) -> list[int]:
    while not update_ordered(list1,dict1):
        shuffle(list1)
    return list1

def sum_reordered(list1: list[list[int]], dict1):
    ordered_sum = 0
    for update in list1:
        if not update_ordered(update,dict1):
            order_update(update,dict1)
            ordered_sum += update[len(update) // 2]
    return ordered_sum

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

    # make a dict with a key for every number
    rules_dict = {}
    for k in range(len(rules_list)):
        if rules_list[k][0] not in rules_dict:
            rules_dict[rules_list[k][0]] = [rules_list[k][1]]
        else:
            rules_dict[rules_list[k][0]].append(rules_list[k][1])

    # Convert the updates into lists
    for k in range(len(updates_list)):
        updates_list[k] = [int(x) for x in updates_list[k].split(",")]

    #print(rules_list)
    #print(updates_list)
    #print(rules_dict)

    print(f"The sum of the middle numbers of the correctly ordered updates is: {sum_ordered(updates_list,rules_dict)}")
    print(f"The sum of the middle numbers of the formerly unordered updates in now correct order is: {sum_reordered(updates_list,rules_dict)}")


    test_updates = [[75,47,61,53,29],[97,61,53,29,13],[75,29,13],[75,97,47,61,53],[61,13,29],[97,13,75,29,47]]
    test_str = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

    test_list = test_str.strip().split("\n")
    for k in range(len(test_list)):
        test_list[k] = test_list[k].split("|")
        test_list[k] = tuple(int(x) for x in test_list[k])

    # make a dict with a key for every number
    test_dict = {}
    for k in range(len(test_list)):
        if test_list[k][0] not in test_dict:
            test_dict[test_list[k][0]] = [test_list[k][1]]
        else:
            test_dict[test_list[k][0]].append(test_list[k][1])

"""
    print("TESTTESTTEST")
    print(test_list)
    print(test_dict)
    for k in test_updates:
        print(update_ordered(k,test_dict))
"""
        
