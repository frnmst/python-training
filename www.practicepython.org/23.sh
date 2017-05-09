#!/usr/bin/env bash

# 23.sh
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Sort files lexigoraphically
cat happynumbers.txt | sort > hn.txt
cat primenumbers.txt | sort > pn.txt

# Get and couunt common lines
comm -12 hn.txt pn.txt | wc -l
