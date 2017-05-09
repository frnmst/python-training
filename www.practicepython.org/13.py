#!/usr/bin/env python3

# 13.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Write a program that asks the user how many Fibonnaci numbers to generate and 
# then generates them. Take this opportunity to think about how you can use 
# functions. Make sure to ask the user to enter the number of numbers in the 
# sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
# where the next number in the sequence is the sum of the previous two numbers 
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

import csv
import urllib.request

def fib(n):
    # Safety first.
    if n > 30:
        return "Aborting. Value too big for recursion."
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_iterative(n):
    i = 3
    f = 1
    prev = 1
    prevprev = 1
    if n == 1 or n == 2:
        return f
    while i <= n:
        f = prev + prevprev
        #print(f)
        #print()
        prevprev = prev
        prev = f

        i+=1

    return f

def test():
    url = 'https://raw.githubusercontent.com/bennacer860/benford_s_law/master/data/fibonacci.csv'
    urllib.request.urlretrieve(url, 'fibonacci.csv')
    with open('fibonacci.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the CSV header
        next(reader, None)
        for row in reader:
            assert fib_iterative(int(row[0])) == int(row[1])

def main():
    test()
    print(fib(int(input("How many Fibonacci numbers do you want? (this may take a long time) "))))
    print(fib_iterative(int(input("How many Fibonacci numbers do you want? (this is efficient) "))))


main()

