class IntervalTree:
    def __init__(self, intervals):
        # sort the full list of intervals by begin and build the tree
        self.root = self.split_intervals(sort_by_begin(intervals))

    # build the interval tree by recursively splitting the intervals into:
    #    - intervals overlapping with the node center (to be stored in the current node)
    #    - intervals whose end is less than the node center (to be forwarded to the left node)
    #    - intervals whose begin is higher than node center (to be forwarded to the right node)
    def split_intervals(self, intervals):
 
        if not intervals:
            return None
 
        x_center = self.center(intervals)
 
        s_center = []
        s_left = []
        s_right = []
 
        for k in intervals:
            if k.get_end() < x_center:
                s_left.append(k)
            elif k.get_begin() > x_center:
                s_right.append(k)
            else:
                s_center.append(k)
 
        return Node(x_center, s_center, self.split_intervals(s_left), self.split_intervals(s_right))

    # find the node center (begin of the interval in the middle of the sorted list of intervals) 
    def center(self, intervals):
        return intervals[int(len(intervals)/2)].get_begin()
    
    # count the intervals overlapping with x by traversing the tree
    def overlap_counts(self, node, x):
        
        if(node == None):
            return 0
        
        if x == node.x_center:
            return len(node.s_center_begin_sorted)
        else:
            count = 0
            
            if x < node.x_center: # check into the center list then recurse into the left child
                for n in node.s_center_begin_sorted:
                    if n.get_begin() <= x:
                        count = count + 1
                    else:
                        break
                return count + self.overlap_counts(node.left_node, x)
            else: # check into the center list then recurse into the right child
                for n in node.s_center_end_sorted: 
                    if n.get_end() >= x:
                        count = count + 1
                    else:
                        break
                return count + self.overlap_counts(node.right_node, x)
            
 
  
class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def get_begin(self):
        return self.begin
    def get_end(self):
        return self.end

    
class Node:
    def __init__(self, x_center, s_center, left_node, right_node):
        self.x_center = x_center # node center
        self.s_center_begin_sorted = s_center # s_center is already sorted by begin
        self.s_center_end_sorted = sort_by_end(s_center) # store a copy of center list by ending reverse order to speed up the counting
        self.left_node = left_node
        self.right_node = right_node

#
# utility functions to sort the list of intervals by begin (asc) or end (desc)
#
def sort_by_begin(intervals):
        return sorted(intervals, key=lambda x: x.get_begin())

def sort_by_end(intervals):
    return sorted(intervals, key=lambda x: x.get_end(), reverse = True)