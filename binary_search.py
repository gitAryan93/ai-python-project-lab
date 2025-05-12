def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        print(f"Checking index {mid}: {arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ======TRY IT OUT ======
arr = [2, 3, 3, 4, 5, 6, 7, 15, 33, 66]
target = int(input("Enter number to search for: "))
result = binary_search(arr, target)

if result != -1:
    print(f"✅ Found at index {result}")
else:
    print("❌ Not found.")
