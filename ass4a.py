# Fibonacci series upto n terms using loop 

# n = int(input(" Enter the number of terms : "))

def fibonacci(n) : 
  fib_series = []

  a, b = 0 , 1

  for _ in range(n) :
    fib_series.append(a)
    a, b = b  , a+b

  return fib_series



term = int(input("Enter the term : "))

print(fibonacci(term))
