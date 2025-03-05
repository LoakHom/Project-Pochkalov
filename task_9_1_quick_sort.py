import sys
from typing import List

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    try:
        input_data = list(map(int, sys.stdin.readline().strip().split()))
        sorted_data = quicksort(input_data)
        print(" ".join(map(str, sorted_data)))
    except ValueError:
        print("Ошибка: Введите список целых чисел, разделенных пробелами.")
