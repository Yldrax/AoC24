"""
    December 02, 2024

"""

"""
    Part 01
"""
def check_safety(list1) -> bool:
    ascending = False
    descending = False
    safe = True

    for i in range(len(list1) - 1):
        if abs(list1[i] - list1[i + 1]) > 3 or list1[i] - list1[i + 1] == 0:
            safe = False
            break
        elif list1[i] < list1[i + 1]:
            ascending = True
            if descending:
                safe = False
                break
        else:
            descending = True
            if ascending:
                safe = False
                break

    return safe

def check_report_safeties(list1):
    safe_num = 0

    for sublist in list1:
        if check_safety(sublist):
            safe_num += 1

    return safe_num

"""
    Part 02
"""
def check_dampened_safety(list1) -> bool:
    safe = False
    for i in range (len(list1)):
        sublist = list1.copy()
        sublist.pop(i)
        if check_safety(sublist):
            safe = True
            break

    return safe

def check_dampened_report_safeties(list1):
    safe_num = 0

    for sublist in list1:
        if check_safety(sublist):
            safe_num += 1
        elif check_dampened_safety(sublist):
            safe_num += 1

    return safe_num


"""
    Using the Functions
"""

if __name__ == '__main__':

    # Getting the String
    file = open('inputs/02.txt', 'r')
    input_str = file.read()
    file.close()

    # Splitting and type casting the String into nested lists of integers
    input_list = input_str.strip().split("\n")
    for k in range(len(input_list)):
        input_list[k] = input_list[k].split(" ")
    for l in range(len(input_list)):
        input_list[l] = [int(x) for x in input_list[l]]

    print(f"The number of safe reports is {check_report_safeties(input_list)}.")
    print(f"The number of safe reports with dampening is {check_dampened_report_safeties(input_list)}.")