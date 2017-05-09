#!/usr/bin/env python3

# 03.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

CONST = 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]

print("a = " + str(a))
for i in a:
    if i < CONST:
        print ("Element " + str(i) + " in list is less than " + str(CONST))
        b.append(i)

print ("Here in a new purged list with all the previously cited elements")
print ("b = " + str(b))

# Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.
discriminator = input("Input another number: ")

for i in a:
    if i < int(discriminator):
        print ("Element " + str(i) + " in list is less than " + str(discriminator))
