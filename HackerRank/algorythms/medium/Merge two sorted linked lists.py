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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    tmp = -1
    if head1.data < head2.data:
        tmp = head1.data
        head1 = head1.next
    else :
        tmp = head2.data
        head2 = head2.next
    head = current = SinglyLinkedListNode(tmp)
    while head1 != None or head2 != None:
        data = 0
        if head1 == None:
            data = head2.data
            head2 = head2.next 
        elif head2 == None:
            data = head1.data
            head1 = head1.next
        elif head1 and head1.data < head2.data:
            data = head1.data
            head1 = head1.next
        else :
            data = head2.data
            head2 = head2.next 
        current.next = SinglyLinkedListNode(data)
        current = current.next
    return head
if __name__ == '__main__':

    tests = 1

    for tests_itr in range(tests):
        llist1_count = 3

        llist1 = SinglyLinkedList()
        tmp = [1, 2, 3]
        for i in range(llist1_count):
            llist1.insert_node(tmp[i])
            
        llist2_count = 2

        llist2 = SinglyLinkedList()
        tmp = [3, 4]
        for i in range(llist2_count):
            llist2.insert_node(tmp[i])

        llist3 = mergeLists(llist1.head, llist2.head)

