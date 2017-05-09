#!/usr/bin/env python3

# 11.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no 
# divisors.).

def prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        # Skip divisors 1 and self. Step -1
        for n in range(number-1, 1, -1):
            if number % n == 0:
                return False

    return True

def main():
    if prime(int(input("Input a number to check for primality: "))):
        print ("Input number is prime")
    else:
        print ("Input number is NOT prime")

def test():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 131072]
    for p in primes:
        assert prime(p)
    for q in non_primes:
        assert not prime(q)

    print ("Tests verified")

#main()
test()
