#!/usr/bin/env python

import sys

def readIntervalsFile(fileName):
    file = sys.argv[1]
    with open(file) as f:
        lines = f.readlines()
    return lines

def countIntervals(num):
    file = sys.argv[1]
    intervals = readIntervalsFile(file)
    count = 0
    for interval in intervals:
        lower, higher = interval.split()
        if int(lower) <= num and num <= int(higher):
            count = count + 1
    print(count)

def processLine(line):
    if line is not '':
        num = int(line)
        countIntervals(num)

def main():
    for line in sys.stdin:
        processLine(line)

if __name__ == "__main__": main()
