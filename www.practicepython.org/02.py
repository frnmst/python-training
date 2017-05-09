#!/usr/bin/env python3

# 02.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

print ("Hello, I'll tell you if the input number is even or odd.")
number = input ("Number: ")
print ("The number you provided me, " + str(number) + ", is ", end='')
if (int(number) % 2) == 0:
    print("even")
    if(int(number) % 4) == 0:
        print("It's also a multiple of 4")
else:
    print("odd")

print ("Check that two numbers are divisible (first divides into second)")
num=input("First: ")
check=input("Second: ")

print (num + " and " + check + " are ", end='')
if int(num) % int(check) == 0:
    print('',end='')
else:
    print ('not ',end='')

print ("divisible")
