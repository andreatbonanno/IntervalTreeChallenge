#!/usr/bin/env bash

# optional argument indicates the extension to use
ex=$1
if [ -z $ex ]; then
  ex=py
fi

x=1
while [ -f "fixtures.$x.intervals.txt" ] && [ -f "fixtures.$x.numbers.txt" ] && [ -f "fixtures.$x.output.txt" ]
do
  ./intervals.$ex fixtures.$x.intervals.txt < fixtures.$x.numbers.txt | cmp fixtures.$x.output.txt - || exit 1;
  x=$(( $x + 1 ))
done
