#!/usr/bin/env python3

# 01.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

from datetime import date


name = input('Your name: ')
age = input('Your age: ')
centenary=str((date.today().year - int(age)) + 100)

output=name + ', you will turn 100 on the year ' + centenary
print (output)

repeat = int(input('Input a new number: '))

print (repeat * (output + '\n'))

