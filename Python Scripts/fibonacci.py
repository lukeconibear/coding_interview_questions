def get_nth_fib(n):  # time O(2^n), space O(n as n calls to fib on call stack)
    if n == 1:
        return 0
    if n == 2:
        return 1
    return get_nth_fib(n - 1) + get_nth_fib(n - 2)
