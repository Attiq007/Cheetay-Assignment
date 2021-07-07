# Time Complexity : O(nlogn)
# Auxiliary Space : O(n)
def activityselection(start, end, n):
    if not (start and end):
        return 0

    num_of_activity = 0
    i = 0
    for j in range(n): 
        if start[j] >= end[i]:
            num_of_activity += 1
            i = j
    return num_of_activity
