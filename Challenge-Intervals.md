# Tallarium Interview Challenge - Intervals

## Description

The program `intervals.{js,py}` is called with a single argument, which is the name of a file.
It reads all subsequent input from standard input, (until the EOF character is passed in) and writes to standard output.

```bash
./intervals.{js,py} intervals_file
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
of running `./intervals.{js,py} fixtures.{x}.intervals.txt < fixtures.{x}.numbers.txt`
to `fixtures.{x}.output.txt`:

```bash
./test.sh [js|py]
```

## Your Tasks

Fork this gist. You can choose to modify one of the existing implementations, or write a new one in your favourite language.

### Complexity Analysis

What is the run-time complexity of the current implementation(s)?
Are there any obvious inefficiencies?

### Optimized Algorithm

Can you think of an asymptotically better algorithm? Implement it and analyze its complexity!
Make sure you write clear, well-structured code as it will be used to assess your performance,
as well as the correctness and efficiency of your algorithm and its correct complexity analysis.

### Testing (for bonus points)

Can you think some other useful test cases one would include in a unit testing suite?
Explain your choice.

### Modularisation (for extra bonus points)

How would you split up your solution into multiple files / classes to make it more modular?
If you have time to spare, do it!
