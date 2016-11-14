# IntervalTreeChallenge
Build an interval tree of integers intervals to count the numbers of intervals overlapping each integers contained in the input list.

## Description

The program `intervals.py` is called with a single argument, which is the name of a file.
It reads all subsequent input from standard input, (until the EOF character is passed in) and writes to standard output.

```bash
./intervals.py intervals_file
```

The intervals_file whose name is passed to the program contains a
list of number pairs, representing closed intervals. Each line contains
exactly one closed interval represented as "X WHITESPACE Y". The maximum
size of this file is a million entries, it may contain any number of
duplicates (representing distinct instances of the same interval) and
may or may not end with a NEWLINE.

The program then reads lines from STDIN, potentially billions of lines,
each line containing a single number P and prints to STDOUT on a new line
a single number N, such that N is the number of closed intervals [X, Y]
defined in the intervals_file containing the number P (P is contained within
a closed interval [X, Y] iff X <= P <= Y).

We assume that all numbers are positive integers between 0 and 2147483647.

### Examples

We attach two examples input fixtures, `fixtures.{1,2}.{intervals,numbers}.txt`,
and their corresponding outputs `fixtures.{1,2}.output.txt`.

We also provide a script to run a simple test suite comparing the output
of running `./intervals.py fixtures.{x}.intervals.txt < fixtures.{x}.numbers.txt`
to `fixtures.{x}.output.txt`:

```bash
./test.sh py
```

### Complexity Analysis

What is the run-time complexity of the current implementation(s)?
Are there any obvious inefficiencies?

### Optimized Algorithm

Can you think of an asymptotically better algorithm? Implement it and analyze its complexity!
Make sure you write clear, well-structured code as it will be used to assess your performance,
as well as the correctness and efficiency of your algorithm and its correct complexity analysis.

