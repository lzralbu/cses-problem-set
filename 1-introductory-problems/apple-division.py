n = int(input())
nums = [int(num) for num in input().split(' ')]

total_weight = sum(nums)
subset_weight = 0

minimum_difference = total_weight

def gen_subsets(k):
    global n, nums, total_weight, subset_weight, minimum_difference
    if k == n:
        minimum_difference = min(minimum_difference, abs(total_weight - 2 * subset_weight))
    else:
        subset_weight += nums[k]
        gen_subsets(k + 1)
        subset_weight -= nums[k]
        gen_subsets(k + 1)

gen_subsets(0)

print(minimum_difference)
