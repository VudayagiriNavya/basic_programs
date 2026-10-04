n = int(input())
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range (2, n):
        if n % 2 == 0:
            is_prime = False
            break
if is_prime:
    print(" prime")
else:
    print(" not prime")
       
