# Made by Micha de Groot
# linked list for a single variable polynomial for complex numbers

import sys
# How do I import a module?


# to add two polynomials simply add the coefficients of the nodes with the same degree
# to multiply two polynomials store the product of two coefficients in node with
# degree equal to the sum of the two nodes

# solve for value?
# start with only quadratic functions

class Polynomial:

    def __init__(self, value_pairs):
        self.linked_list = linked_list()
        if not isinstance(value_pairs, list):
            print('Not a valid argument')
            return

        for i in range(len(value_pairs)):
            self.linked_list.add_node(value_pairs[i])
        if self.linked_list.list_length() == 0:
            print('Size 0 polynomial created')


    def test(self):
        self.linked_list.list_print()


# operations needed:
# init
# evaluate
# add two polynomials
# multiply two polynomials
# solve for value


