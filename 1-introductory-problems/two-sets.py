n = int(input())

nums1 = set(range(1, n + 1))
nums2 = set()

total_sum = n * (n + 1) // 2
partial_sum = 0
for i in range(n, 0, -1):
    if 2 * (partial_sum + i) <= total_sum:
        nums1.remove(i)
        nums2.add(i)
        partial_sum += i

if sum(nums1) == sum(nums2):
    print('YES')
    print(len(nums1), '\n', ' '.join(map(lambda x: str(x), nums1)), sep = '')
    print(len(nums2), '\n', ' '.join(map(lambda x: str(x), nums2)), sep = '')
else:
    print('NO')
