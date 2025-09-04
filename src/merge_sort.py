# -*- coding: utf-8 -*-
"""
Project: Merge Sort without Sentinels
Exercise: CLRS 2.3-7*
"""

from typing import List

def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]; i += 1; k += 1
    while j < len(R):
        arr[k] = R[j]; j += 1; k += 1

def merge_sort(arr: List[int], left: int = 0, right: int | None = None) -> None:
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

if __name__ == '__main__':
    sample = [38, 27, 43, 3, 9, 82, 10]
    print('Original:', sample)
    merge_sort(sample)
    print('Sorted:  ', sample)
