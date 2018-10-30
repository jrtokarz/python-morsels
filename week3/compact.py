#!/usr/bin/env python2

# Python Morsels - Week 3 - Compact

def compact(sequence):
    prev_value = UnboundLocalError

    for s in sequence:
        if prev_value != s:
            prev_value = s
            yield s

if __name__ == "__main__":
    print compact([1, 1, 1])
    print compact([1, 1, 2, 2, 3, 2])
    print compact([])
