'''
Andrew Kozempel
CMPSC 412
Lab 9
Fall 2023
'''

import timeit
import random
import time

# node class for BST nodes
class Node:

    # initialize node with val + left/right
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BST class
class BinarySearchTree:

    # initalize BST
    def __init__(self):
        self.root = None

    def insert(self, val):

        # create new node to insert
        node = Node(val)

        # create current pointer for going through nodes
        current = self.root

        # if there's no root yet, root = node
        if not self.root:
            self.root = node
            return

        while True:

            # if new node is less than or equal to current
            if val <= current.val:

                # if no left child, left = node
                if current.left is None:
                    current.left = node
                    return
                
                # point to left child
                current = current.left

            # if new node is greater than current
            elif val > current.val:

                # if no right child, right = node
                if current.right is None:
                    current.right = node
                    return
                
                # point to right child
                current = current.right

# node class for a linked list
class ListNode:

    # initalize node with value and next
    def __init__(self, value):
        self.value = value
        self.next = None

# linked list class
class LinkedList:

    # initalize LL
    def __init__(self):
        self.head = None

    def append(self, value):

        # if empty, insert at beginning (head)
        if self.head is None:
            self.head = ListNode(value)

        # if not empty
        else:

            # current pointer
            current = self.head

            # go through nodes, until the end
            while current.next:
                current = current.next

            # add node to the end
            current.next = ListNode(value)

def generate_ints(quantity):
    
    # lst = []

    # # loop "quantity" times
    # for _ in range(quantity):

    #     rand = random.randint(1,10000) # generate random int

    #     lst.append(rand)

    return [random.randint(1,10000) for _ in range(quantity)]

random_ints = generate_ints(25000)

# list

test_list = []

list_start = time.time()
for ele in random_ints:
    test_list.append(ele)

print(f'Populating list time: {time.time()-list_start:.5f} seconds')

# dict

test_dict = {}

for ele in random_ints:
    test_dict[ele] = len(test_dict)

# BST
# linked list