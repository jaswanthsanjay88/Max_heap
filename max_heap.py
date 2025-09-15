def max_heapify(arr, n, i):
    """
    This function converts a subtree rooted at index i into a Max Heap.
    
    Args:
        arr: The array representation of the binary tree.
        n: The size of the array.
        i: The index of the root of the subtree to be heapified.
    """
    # Initialize the largest element as the root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr, n):
    """
    This function builds a Max Heap from an unsorted array.
    
    Args:
        arr: The unsorted array to be converted.
        n: The size of the array.
    """
    # Start from the last non-leaf node and heapify each subtree
    # The index of the last non-leaf node is (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# --- Main part of the program ---
if _name_ == '_main_':
    # Read the number of elements
    try:
        n_str = input()
        if not n_str.strip():
            # Handle empty line for n
            print("Error: The number of elements (n) cannot be empty.")
        else:
            n = int(n_str)

            # Read the space-separated elements and convert to a list of integers
            arr_str = input()
            arr = list(map(int, arr_str.split()))

            # Check if the number of elements matches the array size
            if len(arr) != n:
                print("Error: The number of elements provided does not match n.")
            else:
                build_max_heap(arr, n)

                # Print the final array, which is now a Max Heap
                print(' '.join(map(str, arr)))

    except (ValueError, IndexError) as e:
        print(f"An error occurred while processing the input: {e}. Please ensure the input format is correct.")
