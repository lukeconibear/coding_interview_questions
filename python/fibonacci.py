def fib_recursive(n):  # time O(2^n), space O(n as n calls to fib on call stack)
    if n == 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):  # time O(n), space O(1)
    if n == 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    previous = 0
    current = 1
    for _ in range(2, n):
        total = current + previous
        previous = current
        current = total

    return total
