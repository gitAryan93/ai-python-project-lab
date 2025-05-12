def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass: {i+1}")
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
            print(arr)
        print("-" * 27)


arr = [2, 1, 5, 3, 66, 8, 5, 8]
print(f"Original list: {arr}")
bubble_sort(arr)
print(f"Sorted list: {arr}")
