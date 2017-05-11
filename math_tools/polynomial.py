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
        self.poly_list = []
        if not isinstance(value_pairs, list):
            print('Not a valid argument')
            return

        for i in range(len(value_pairs)):
            if value_pairs[0] < 0:
                print("Not a valid exponent, skipping element")
            else:
                self.poly_list.append(value_pairs[i])
        self.poly_list = sorted(self.poly_list)

    def evaluate(self, input_value):
        value = 0
        for parameter in self.poly_list:
            value += parameter[1]*(input_value ** parameter[0])
        return value


    def solve(self, value):
#TODO
        if self.poly_list[0][0] == 1:
            # lijn oplossen
        elif self.poly_list[0][0] == 2:
            #abc formule
        elif self.poly_list[0][0] == 3:
            # cardano
        else:
            print("No solution ca be found for 4th degree polynomial")
            return 0
         

# operations needed:
# init
# evaluate
# add two polynomials
# multiply two polynomials
# solve for value


