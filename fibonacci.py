# fib
import time
def fib(n, d):
  if n in d:
    return d[n]
  else:
    d[n] = fib(n-1, d) + fib(n-2, d)
    return d[n]
    
start = time.time()
d = {0:1, 1:1}
fib(40, d)
print(time.time() - start)
