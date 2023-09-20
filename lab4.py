'''
Andrew Kozempel
CMPSC 412
Lab 4
Fall 2023

VIDEO
'''

############################################################
#  PART 1 - Binary Search Guesser
############################################################

# Best: O(1) - mid element
# Worst: O(logn) - first or last
def binary_search(lst):

    # assign left and right indices
    left = 0
    right = len(lst) - 1

    # flag for answer found
    flag = False
    
    # while loop until target is found
    while flag == False:

        # calculate mid index
        mid = (left + right) // 2

        # answer to less than or greater than
        answer = input(f'Is your number less than (1), greater than (2), or equal to (3) {lst[mid]}?')

        # if mid index is target, return index
        if answer == 3:
            return lst[mid]
            flag = True
        
        # search right half if greater than guess
        elif answer == 2:
            left = mid + 1

        # search left half if less than guess
        else:
            right = mid - 1


def generate_ints(quantity, int_list):
    
    # loop "quantity" times
    for x in range(quantity):

        int_list.append(x) # fill list

test_list = []

generate_ints(500,test_list)

test_list.sort()
print(len(test_list))
binary_search(test_list)

############################################################
#  PART 2 - STUDENT SORTING
############################################################

'''
# Best: O(1)
# Worst: O(n)
def student_linear_search(lst, target, key):

    # iterate through list
    for i, student in enumerate(lst):

        # if element is target, return index
        if student[key] == target:
            return i

# Best: O(n)
# Worst: O(n^2)
def student_insertion_sort(lst, key):

    # loop through list starting at second
    for i in range(1, len(lst)):

        curr = lst[i] # store current element
        j = i - 1 # element before curr

        # while there are elements to the left of curr
        # and curr is less than previous element
        while j >= 0 and curr[key] < lst[j][key]:

            lst[j + 1] = lst[j] # move element to the right (copy)
            j -= 1 # move to previous element

        # insert current element in correct spot
        lst[j + 1] = curr
    
    return lst

# Best: O(n^2)
# Worst: O(n^2)
def student_selection_sort(lst, key):

    # iterate through list
    for i in range(len(lst)):

        # initalize min index
        min_idx = i

        # iterate through unsorted elements
        for j in range(i+1, len(lst)):

            # update min index if smaller elements is found
            if lst[j][key] < lst[min_idx][key]:
                min_idx = j

        # swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    return lst

# Best: O(n)
# Worst: O(n^2)
def student_bubble_sort(lst, key):

    # length of list
    n = len(lst)

    # iterate through list
    for i in range(n):

        # flag to track swaps
        swapped = False

        # iterate through unsorted (ignore the last i elements)
        for j in range(0, n-i-1):

            # swap if out of order
            if lst[j][key] > lst[j+1][key]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True # swap is true

        # break if swapped (sorted)
        if not swapped:
            break

    return lst

# Read file
def read_student_data(filename):
    # store student data
    students = []
    # open the file in read mode
    with open(filename, 'r') as file:
        # read first line to get the headers/column names
        headers = file.readline().strip().split(',')
        
        # loop through each line in the file
        for line in file:
            # split the line into individual data items
            data = line.strip().split(',')
            
            # create a dictionary for each student using a dictionary comprehension
            student = {}
            
            # iterate through items in line
            for i in range(len(headers)):
                student[headers[i]] = data[i]
            
            # append the student dictionary to the students list
            students.append(student)
    
    # return the list of student dictionaries
    return students

students_data = read_student_data('students.txt')'''