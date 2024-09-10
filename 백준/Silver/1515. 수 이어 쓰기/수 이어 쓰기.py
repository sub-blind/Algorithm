nums = input().strip()
i = 0
index = 0

while index < len(nums):
    i += 1
    num = str(i)
    
    for char in num:
        if char == nums[index]:
            index += 1
            if index == len(nums):
                print(i)
                break
