def SumOddUpToN(n):
    total = 0
    for i in range(1, n + 1, 2): 
        total += i
    return total

print("Enter N: ")
n_input = input()
n = int(n_input)
print("Sum of odd numbers up to N: ", SumOddUpToN(n))