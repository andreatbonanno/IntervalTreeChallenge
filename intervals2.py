import sys
from interval_tree import Interval, IntervalTree

def readIntervalsFile():
    file = sys.argv[1]
    with open(file) as f:
        lines = f.readlines()
    return lines

def processLine(tree,line):
    if line is not '':
        print(tree.overlap_counts(tree.root,int(line)))

def str_to_interval(str_list):
    intervals = []
    for s in str_list:
        lower, higher = s.split()
        intervals.append(Interval(int(lower), int(higher)))
    return intervals

def main():
    # build intervals list from file
    intervals = str_to_interval(readIntervalsFile())
    # build an interval tree
    tree = IntervalTree(intervals)

    for line in sys.stdin:
        # search input number in tree
        processLine(tree, line)

if __name__ == "__main__": main()