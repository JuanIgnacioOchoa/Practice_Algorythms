#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    s = set()
    while head1 != None or head2 != None:
        if head1 != None:
            if head1 in s:
                return head1.data
            else :
                s.add(head1)
            head1 = head1.next
        if head2 != None:
            if head2 in s:
                return head2.data
            else:
                s.add(head2)
            head2 = head2.next
    return


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = 1#int(input())

    for tests_itr in range(tests):
        index =2#int(input())

        llist1_count = 3#int(input())

        llist1 = SinglyLinkedList()

        for i in [1, 2, 3]:
            #llist1_item = int(input())
            llist1.insert_node(i)
            
        llist2_count = 1#int(input())

        llist2 = SinglyLinkedList()

        for i in [1]:
            #llist2_item = int(input())
            llist2.insert_node(i)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        #fptr.write(str(result) + '\n')

    #fptr.close()

    