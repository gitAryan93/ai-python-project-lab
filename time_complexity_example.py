def constant_time_example():
    arr = [10, 20, 30, 40, 50]
    # Always takes the same time, no matter how big arr is
    print("Accessing index 3:", arr[3])


constant_time_example()


def linear_time_example():
    arr = list(range(1, 6))
    for num in arr:
        print(f"Value: {num}")


def quadratic_time_example():
    arr = list(range(1, 6))
    for i in arr:
        for j in arr:
            print(f"Pair: ({i}, {j})")


def exponential_time_example(n):
    if n <= 1:
        return n
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)


constant_time_example()
linear_time_example()
quadratic_time_example()
print("Fibonacci(5):", exponential_time_example(5))
