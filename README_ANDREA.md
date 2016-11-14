## Inefficiencies with intervals.py
	* multiple access to files, one for each line from STDIN
	* no need to read the argument in readIntervalsFile
	* complexity is asymptotically O(n * m) with n parameters from stdin and m lines in the file, 
	  because for each parameters from STDIN the whole file is read and each line is checked against the parameters

## How can we improve the complexity?
	* read the file once at the beginning and build an interval tree to store intervals. 
	* The interval tree has an overall creation complexity of O(m * (log m)), with m lines in the file (i.e., number of intervals).
	* The complexity of a single search is O((log m) + k), with 0 <= k <= m the number of 
	  overlapping intervals. For n parameters from STDIN the complexity is O(n * ((log m) + k_n)). Only in the wrst case of having each of the n points overlapping with all the intervals, the complexity of the interval tree solution would be as bad as the complexity of the first naive solution.
	* SEE THIS SOLUTION IMPLEMENTED IN intervals2.py

## Other useful test cases may include:
	* for each interval check Y >= X
	* for each interval, check len(interval.split) == 2