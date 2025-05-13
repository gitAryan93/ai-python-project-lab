def factorial(n):
    print(f"Calling factorial ({n})")

    if n == 1:
        print(f"Reached base case: factorial(1) = 1")
        return 1
    else:
        result = n * factorial(n-1)
        print(f"Returning {n} * factorial({n-1}) = {result}")
        return result


# Try it
print("final Anwer:", factorial(5))
