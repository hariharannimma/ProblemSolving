nums = [2, 7, 11, 15]
target = 9
hashmap = dict()
for i in range(len(nums)):
    if nums[i] in hashmap:
        print(hashmap[nums[i]], i)
    else:
        hashmap[target-nums[i]] = i
