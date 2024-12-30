# use the concept of high orderer filtered functions to generate a list of all prime numbers from 251 to 5050 in reverse order

numbers = range(251, 5051)

def allPrime(num) :
    if num < 2 :
        return False
    
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0:
            return False
        return True

primeList = list(filter(allPrime, numbers))

primeList.reverse()

print(f"All prime numbers: {primeList}")