#!/usr/bin/env python3

# 12.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 
# 20, 25]) and makes a new list of only the first and last elements of the 
# given list. For practice, write this code inside a function.

def destroys_original(list):
    result = []
    result.append(list.pop(0))
    result.append(list.pop())
    # Equivalent:
    # result.append(list.pop(len(list)-1)))
    return result

def keeps_original(list):
    result = []
    result.append(list[0])
    result.append(list[len(list)-1])
    return result

# Website solution.
def website_solution(list):
    return [list[0], list[len(list)-1]]

def main():
    a = [5, 10, 15, 20, 25]
    print(website_solution(a))
    print(keeps_original(a))
    print(destroys_original(a))
    print(a)

main()
