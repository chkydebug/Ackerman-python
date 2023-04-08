def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

# Get user input for m and n
m = int(input("Enter a non-negative integer value for m: "))
n = int(input("Enter a non-negative integer value for n: "))

# Call the ack function with user input values
result = ack(m, n)

# Print the result
print("The result of the Ackermann function for m = {} and n = {} is: {}".format(m, n, result))