"""
Baekjoon 5639 이진 검색 트리

"""

""" Wrong Code
tree = [-1] * 10001
tree[0] = 1000001
tree[1] = int(input())
current_node = 1

while True:
    try:
        input_node_value = int(input())
        if tree[current_node] > input_node_value:
            current_node *= 2
            tree[current_node] = input_node_value
        else:
            while tree[current_node] < input_node_value:
                if current_node % 2 == 1:
                    current_node = int(current_node / 4)
                else:
                    current_node = int(current_node / 2)
            if current_node == 0:
                current_node = 1
            while tree[current_node] != -1:
                if tree[current_node] < input_node_value:
                    current_node = current_node * 2 + 1
                else:
                    current_node *= 2
            tree[current_node] = input_node_value
    except EOFError:
        break


def postorder_traverse(node):
    if tree[node] == -1:
        return
    postorder_traverse(node * 2)
    postorder_traverse(node * 2 + 1)
    print(tree[node])


postorder_traverse(1)
"""

""" Wrong Code
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


root = Node(int(input()))

while True:
    try:
        input_node_value = int(input())
        root.insert(input_node_value)
    except EOFError:
        break


def postorder_traverse(node):
    if node is None:
        return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.value)


postorder_traverse(root)
"""

import sys
sys.setrecursionlimit(10 ** 9)

input_node_value = []

while True:
    try:
        input_node_value.append(int(input()))
    except EOFError:
        break


def preorder_to_postorder(start, end):
    if start > end:
        return
    parent_value = input_node_value[start]
    right_child = end + 1
    for i in range(start + 1, end + 1):
        if parent_value < input_node_value[i]:
            right_child = i
            break
    if right_child is not start + 1:
        preorder_to_postorder(start + 1, right_child - 1)
    if right_child is not end + 1:
        preorder_to_postorder(right_child, end)
    print(parent_value)


preorder_to_postorder(0, len(input_node_value) - 1)
