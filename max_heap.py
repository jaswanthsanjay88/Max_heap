import sys


def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def main():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        arr = list(map(int, sys.stdin.readline().split()))
        build_max_heap(arr, n)
        print(*arr)
    except (ValueError, IndexError):
        return


if _name_ == "_main_":
    main()
