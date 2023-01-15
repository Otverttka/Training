"""
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.
"""
def digital_root(n):
    num = n
    while len(str(num)) > 1:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        num = sum
    return num

print(digital_root(493193))