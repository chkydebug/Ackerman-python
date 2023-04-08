# Ackerman-python
A generic Ackerman function to determine the maximum depth of recursion.
The algorithm first checks whether m is zero. If it is, the function returns n + 1. Otherwise, it checks whether m is greater than zero and n is zero. If so, the function recursively calls itself with m - 1 and 1 as arguments. Finally, if both m and n are greater than zero, the function recursively calls itself with m - 1 and the result of another call to ackermann with m and n - 1 as arguments.

It's worth noting that the Ackermann function grows very quickly as m and n increase, so it is not practical to compute the function for large values of m and n using this algorithm. In fact, the function grows faster than any computable function, which makes it useful for studying the limits of computation
