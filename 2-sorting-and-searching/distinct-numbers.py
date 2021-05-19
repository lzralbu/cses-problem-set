n = int(input())
nums = [int(word) for word in input().split(' ')]
nums.sort()
total_equal_nums = 0
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        total_equal_nums += 1
print(len(nums) - total_equal_nums)
