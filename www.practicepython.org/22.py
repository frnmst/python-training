#!/usr/bin/env python3

# 22.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.


# Given a .txt file that has a list of a bunch of names, count how many of each 
# name there are in the file, and print out the results to the screen. I have a 
# .txt file for you, if you want to use it!
# Extra: Instead of using the .txt file from above (or instead of, if you want 
# the challenge), take this .txt file, and count how many of each “category” of 
# each image there are. This text file is actually a list of files 
# corresponding to the SUN database scene recognition database, and lists the 
# file directory hierarchy for the images. Once you take a look at the first 
# line or two of the file, it will be clear which part represents the scene category. To do this, 
# you’re going to have to remember a bit about string parsing in Python 3. I 
# talked a little bit about it in this post.

# Python dictonaries == Bash associative arrays

def print_dictionary(dictionary):
    for name, frequency in dictionary.items():
        print(name + "          " + str(frequency) + " occurrencies")

    # No direct sorting function is possible: either use OrderedDict object?
    # or transform the dictionary in two lists: 1 values, 1 keys.
    # Sort values list by values (increasing or decreasing) and at the same 
    # time do the same operations on the keys list.
    #
    # Example with increasing sort:
    #
    # keys = ['a', 'b', 'c', 'd']
    # values = ['7', '1', '9', '0']
    #
    # ->
    #
    # keys = ['d', 'b', 'a', 'c']
    # values = ['0', '1', '7', '9']
    #
    # Sequential print of both lists


    # Failed attempts:
    #
    #for k in sorted(dictionary.values(), reverse=True):
    #    print(k)
    #
    # out = sorted(dictionary, key=lambda x : dictionary[x]) 
    # print(out)

# name = key, frequency = value.
def counter(name,dictionary):
        dictionary[name] += 1

def new_element(name,dictionary):
    dictionary[name] = 0

def add(name,dictionary):
    if name not in dictionary:
        new_element(name,dictionary)
    counter(name,dictionary)

# A category is defined as the line's substring before the last '/'
# character.
def get_category(line):
    category_separator = '/'

    return line[0:line.rfind(category_separator)]


def count_occurrencies(filename,is_category):
    dictionary = dict()
    read_file(filename,dictionary,is_category)
    print_dictionary(dictionary)

# Remove newlines while looping to avoid problems.
def read_file(filename,dictionary,is_category):
    with open(filename, 'r') as storage:
        for line in storage:
            # print(line)
            if is_category:
                add(get_category(line.strip()),dictionary)
            else:
                add(line.strip(),dictionary)


## Test functions

# Just print the input list as dictionary.
def test_dict_printing(list_as_dict):
    print_dictionary(dict(list_as_dict))

def test_counter(list):
    result_dictionary = dict([('a', 0), ('b', 0), ('c', 0), ('d', 0)])
    for e in list_as_dict:
        counter(e,result_dictionary)
    print(result_dictionary)

def test_new_element(list):
    result_dictionary = dict()
    for e in list:
        new_element(e,result_dictionary)
    print(result_dictionary)

def test_real_add(list):
    result_dictionary = dict()
    # This for loop correspond to the line by line file scanning.
    for e in list:
        add(e,result_dictionary)
    print(result_dictionary)


# No test for the category grabber.
def test():
    list_as_dict = [('a', 1), ('b', 3)]
    list_as_dict.append(('c', 2))

    list = ['a', 'b', 'c', 'd', 'a', 'b', 'a', 'd']

    test_dict_printing(list_as_dict)
    test_counter(list)
    test_new_element(list)
    test_real_add(list)

### main ###

# You can do a manual test with grep -c <pattern> <filename> and compare the
# values
if __name__ == '__main__':
    # test()
    count_occurrencies('nameslist.txt',False)
    count_occurrencies('Training_01.txt',True)

