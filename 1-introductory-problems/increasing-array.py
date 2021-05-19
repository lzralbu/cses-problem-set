n = int(input())
nums = [int(num) for num in input().split(' ')]

move_count = 0
i = 0
while i < n - 1:
    if nums[i] > nums[i + 1]:
        move_count += nums[i] - nums[i + 1]
        nums[i + 1] = nums[i]
    i += 1

print(move_count)
