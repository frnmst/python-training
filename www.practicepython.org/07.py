#!/usr/bin/env python3

# 07.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 
# 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a 
# new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Traditional way
res = []
for i in a:
    if i % 2 == 0:
        res.append(i)

print(a)
print(res)

# One liner (seems less readable)
# See https://wiki.python.org/moin/Powerful%20Python%20One-Liners
res = [i for i in a if i % 2 == 0]

print(res)
