def insertion_sort(arr):
    """
    Performs insertion sort on the given array.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    # Make a copy of the array to avoid modifying the original
    arr = arr.copy()
    
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        # Element to be compared
        key = arr[i]
        
        # Compare current element with sorted portion and shift elements
        j = i - 1
        second_key = arr[j]
        
        while j > -1 and second_key > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        # Place current element in its correct position
        arr[j + 1] = key
        
    return arr

# Demonstration with different cases
if __name__ == "__main__":
    # Best case: Already sorted array
    # best_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print("Best case (already sorted):")
    # print("Original array:", best_case)
    # print("Sorted array:", insertion_sort(best_case))
    
    # Worst case: Reverse sorted array
    worst_case = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\nWorst case (reverse sorted):")
    print("Original array:", worst_case)
    print("Sorted array:", insertion_sort(worst_case))
    
    # Average case: Random order array
    average_case = [5, 2, 9, 1, 7, 6, 3, 8, 4, 10]
    print("\nAverage case (random order):")
    print("Original array:", average_case)
    print("Sorted array:", insertion_sort(average_case))
