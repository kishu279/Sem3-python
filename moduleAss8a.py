import math

def isPrime(num) :
    if num < 2 :
        return False
    
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    
    return True

def isPalindrome(num):
    num_str = str(num)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False