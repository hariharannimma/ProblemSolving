nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#nums = [3,0,1]
#nums = [0,1]
#nums = [0]
len_num = len(nums)
sumOfnums = sum(nums)
"""if len(nums) == 1:
    missing_number = 1
else:
    ideal_list = list()
    for i in range(1, len_num+1):
        ideal_list.append(i)
    for i in range(len_num):
        if ideal_list[i] not in nums:
            missing_number = ideal_list[i]
print(missing_number)"""
ideal_list = list()
for i in range(1, len_num+1):
    ideal_list.append(i)
expectedsum = sum(ideal_list)
missing_number = expectedsum - sumOfnums
print(missing_number)
