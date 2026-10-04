arr = list(map(int, input().split()))
even = 0 
odd = 0
for num in arr:
    if num %2 == 0:
        print("even")
    else:
        print("odd")