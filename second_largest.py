nums = list(map(int, input().split()))
largest = nums[0]
second_largest = float( ' -inf ')
for num in nums:
    if num > largest:
        second_largest = largest 
        largest = num
    elif num > second_largest and num!= largest:
         second_largest = num
print(" second_largest", second_largest)