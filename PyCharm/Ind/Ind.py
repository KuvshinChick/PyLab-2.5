#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    sq = tuple(map(float, input("Enter country sizes: ").split()))
    p = tuple(map(float, input("Enter country population: ").split()))

    # Checking the size of a tuple
    if len(sq) != 28 or len(p) != 28:
        print("Invalid tuple size ", file=sys.stderr)
        exit(1)

    # Checking for negative numbers in a tuple "sq"
    for i in sq:
        if i <= 0:
            print("Country size can`t be less than 0 ", file=sys.stderr)
            exit(1)

    # Checking for negative numbers in a tuple "p"
    for i in p:
        if i <= 0:
            print("Country population can`t be less than 0 ", file=sys.stderr)
            exit(1)

    A = int(input("Enter А: "))

    # Adding elements from the tuple "p" by the indices of matching elements from the tuple "sq"
    S = sum(p[sq.index(i)] for i in sq if i < A)
    print(f'Sum of elements: {S}')
