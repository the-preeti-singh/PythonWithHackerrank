import numpy as np

n, m = map(int, input().split())
nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

np.set_printoptions(sign=' ')
nums = np.array(nums)

print(np.mean(nums, axis=1))
print(np.var(nums, axis=0))
print(np.round(np.std(nums), 12))
