import random
import time

# Binary search algorithm

# Naive search: scans entire list and asks if each element is equal to the target
# if yet, it will return the index of the element
# if no, then it will return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search will sort the list by ascending order
# Binary search will separate list into two halves and ask if the target is in the first half or the second half
# if it is in the first half, it will ask if the target is in the first half of the first half or the second half of the first half
# Binary search will continue this pattern until it finds the target or it reaches the end of the list
# if it reaches the end of the list and it still hasn't found the target, it will return -1

def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else: 
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    
    length  = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(0, length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")

