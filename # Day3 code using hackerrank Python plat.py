# Day3 code using hackerrank Python platform
# say "Hello, World!"

print("Hello, World!")

# if else statement

import math
import os
import random
import re
import sys




n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# Arithmetic Operators

a = int(input().strip())
b = int(input().strip())


print(a + b)   # Sum
print(a - b)   # Difference
print(a * b)   # Product


# Integer division

a = int(input().strip())
b = int(input().strip())

print(a // b)

# Float division
print(a / b)

# loops 

# Read integer from input
n = int(input().strip())

# Loop through all non-negative integers less than n
for i in range(n):
    print(i ** 2)

