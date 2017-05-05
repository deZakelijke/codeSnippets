# Made by Micha de Groot
# Implementation of singly linked list

class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def list_node_data(self):
        return self.data

class linked_list:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_node(self, data):
        new_node = Node()
        new_node.data = data

        if (self.head_node is None):
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def pop_tail(self):
        if self.head_node is None:
            return None
        node = self.head_node
        while not node.next is self.tail_node:
            node = node.next
        self.tail_node = node
        node = node.next
        self.tail_node.next = None
        return node

    def list_print(self):
        node = self.head_node
        while node:
            print(node.data)
            node = node.next

    def list_head(self):
        return sef.head_node

    def list_length(self):
        length = 0
        node = self.head_node
        while node:
            length += 1
            node = node.next
        return length

    # Possible extensions for the class
    # def list_next()
    # def list_prev()
    # def lit_insert_before()
    # def lit_insert_after()
    # def list_unlink node()
