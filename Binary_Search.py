import random
import time

def naive_search(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return i
    return -1

def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    length = 10000
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

    start = time.time()
    for num in sorted_list:
        naive_search(sorted_list, num)
    print("Naive search time:", time.time() - start, "seconds")

    start = time.time()
    for num in sorted_list:
        binary_search(sorted_list, num)
    print("Binary search time:", time.time() - start, "seconds")
