
nums = [-10,-12,-54,-12,-544,-10000]
n = len(nums)
numCheck = [0] * n
for i in range(n):
    numCheck[i] = abs(0 - nums[i])
    w = 0
for j in range(n - 1):
    if numCheck[j] > numCheck[j + 1] and numCheck[j+1] < numCheck[w]:
        w = j + 1
    elif numCheck[j] == numCheck[j + 1]:
        if nums[j] < nums[j + 1]:
             w = j + 1

print(nums[w])

