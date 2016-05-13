#!/usr/bin/python
import sys

pre_key = None
lefts = list()
rights = list()
# initial two list to restore data under same key

for line in sys.stdin:


    # get information
    key, tag_values = line.strip().split('\t', 1)
    tag, values = tag_values.strip().split('|', 1)

    # print all tuples when meet new entrance
    if key != pre_key:
        if lefts and rights:
            for left in lefts:
                for right in rights:
                    print ("%s,%s" % (pre_key, left + ',' + right))
        # initialization
        lefts = list()
        rights = list()

    if tag == 'L':
        lefts.append(values)
    elif tag == 'R':
        rights.append(values)

    # update current_key
    pre_key = key


# print the last information
if lefts and rights:
    for left in lefts:
        for right in rights:
            print ("%s,%s" % (pre_key, left + ',' + right))
