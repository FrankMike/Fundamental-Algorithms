from sys import maxsize


# Linked List structure
class Node:
    def __init__(self, d) -> None:
        self.data = d
        self.next = None


# Kadane's Algorithm
def kadane(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, size):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    print(f"Maximum contiguous sum is {max_so_far}")
    print(f"Starting index {start}")
    print(f"Ending index {end}")


# Floyd Cycle Detection Algorithm
def floyd_cycle_detection(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    if detect_loop(head):
        print("Loop exists in the Linked List")
    else:
        print("Loop doesn't exists in the Linked List")


def detect_loop(head):
    slow_pointer = head
    fast_pointer = head
    while slow_pointer is not None and fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return 1
    return 0


# KMP Algorithm
def kmp(pat, txt):
    m = len(pat)
    n = len(txt)
    lps = [0]*m
    j = 0
    compute_lps_array(pat, m, lps)
    i = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            print(f'Found pattern at index {str(i-j)}')
            j = lps[j-1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def compute_lps_array(pat, m, lps):
    l = 0
    i = 1
    while i < m:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1


# Quick Select Algorithm
def quick_select(arr, l, r, k):
    if 0 < k <= r-l+1:
        index = partition(arr, l, r)
        if index - l == k - 1:
            return arr[index]
        if index-l > k-1:
            return quick_select(arr, l, index-1, k)
        return quick_select(arr, index+1, r, k-index+l-1)
    print("Index out of bound")


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# Boyer-Moore Majority Vote Algorithm
def boyer_moore(arr, n):
    candidate = -1
    votes = 0
    for i in range(n):
        if votes == 0:
            candidate = arr[i]
            votes = 1
        else:
            if arr[i] == candidate:
                votes += 1
            else:
                votes -= 1
    count = 0
    for i in range(n):
        if arr[i] == candidate:
            count += 1
    if count > n // 2:
        return candidate
    else:
        return -1
