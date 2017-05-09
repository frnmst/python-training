#!/usr/bin/env python3

# 04.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Create a program that asks the user for a number and then prints out a list 
# of all the divisors of that number. (If you don’t know what a divisor is, it 
# is a number that divides evenly into another number. For example, 13 is a 
# divisor of 26 because 26 / 13 has no remainder.)

divisor_list = []
dividend = input("Input a dividend: ")

for divisor in range(1, int(dividend)+1):
    if int(dividend) % int(divisor) == 0:
        divisor_list.append(divisor)

print("divisor_list = " + str(divisor_list))
